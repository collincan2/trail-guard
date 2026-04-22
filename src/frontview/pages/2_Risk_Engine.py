import streamlit as st
import pandas as pd
import json
import os
import sys

# Connect to the src folder
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from risk_engine import analyze_segment_risk

st.set_page_config(page_title="Risk Engine", layout="wide")
st.title(" Risk Engine & Hazard Database")

# Use 3 tabs now, placing the Overview front and center for the demo
tab1, tab2, tab3 = st.tabs(["Park-Wide Overview", "Live Risk Analysis", "Hazard Database"])

# --- TAB 1: Park-Wide Overview ---
with tab1:
    st.markdown("### Park-Wide Segment Overview")
    st.markdown("At-a-glance view of current risk metrics and escalation states across all trails.")
    
    overview_data = []
    with st.spinner("Compiling park-wide metrics..."):
        # Loop through all 7 segments to gather live data
        for seg_id in range(1, 8):
            data = analyze_segment_risk(seg_id)
            if "error" not in data:
                overview_data.append({
                    "Segment": f"Segment {data['segment_id']} - {data['segment_name']}",
                    "Reports (48h)": data['reports_48h'],
                    "Risk Score": data['risk_score'],
                    "Escalation State": " ESCALATED" if data['escalation_triggered'] else " Safe"
                })
    
    if overview_data:
        df_overview = pd.DataFrame(overview_data)
        
        # Color-coding logic for the table rows
        def highlight_risk(row):
            if row['Risk Score'] >= 10.0:
                return ['background-color: rgba(255, 75, 75, 0.2)'] * len(row) # Red
            elif row['Risk Score'] >= 5.0:
                return ['background-color: rgba(255, 204, 0, 0.2)'] * len(row) # Yellow
            else:
                return ['background-color: rgba(75, 255, 75, 0.1)'] * len(row) # Green
        
        # Apply the colors and format the score to 1 decimal place
        styled_df = df_overview.style.apply(highlight_risk, axis=1).format({"Risk Score": "{:.1f}"})
        
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No hazard data found. Run analysis to generate data.")

# --- TAB 2: Live Risk Analysis ---
with tab2:
    st.markdown("###  Evaluate Live Segment Risk")
    st.markdown("Select a segment to run the deterministic scoring algorithm and trigger AI escalations if necessary.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_seg = st.selectbox("Select Trail Segment to Analyze:", [1, 2, 3, 4, 5, 6, 7])
        analyze_btn = st.button("Calculate Risk Score")
        
    if analyze_btn:
        with st.spinner("Calculating deterministic metrics..."):
            data = analyze_segment_risk(selected_seg)
            
            if "error" in data:
                st.error(data["error"])
            else:
                st.markdown(f"#### Results for Segment {data['segment_id']}: {data['segment_name']}")
                
                m1, m2, m3 = st.columns(3)
                m1.metric("48-Hour Reports", data['reports_48h'])
                m2.metric("Location Multiplier", f"{data['multiplier']}x")
                
                score_color = "normal" if data['risk_score'] < 10.0 else "inverse"
                m3.metric("Cumulative Risk Score", f"{data['risk_score']:.1f}", delta_color=score_color)

                st.markdown("---")
                
                if data['escalation_triggered']:
                    st.error("RISK ESCALATION TRIGGERD")
                    st.warning(f"**AI Dispatch Note:** {data['escalation_note']}")
                else:
                    st.success("Segment is currently operating within acceptable safety parameters.")

# --- TAB 3: Hazard Database ---
with tab3:
    db_path = os.path.join(src_dir, "hazard_db.json")
    
    if os.path.exists(db_path):
        with open(db_path, "r") as f:
            raw_data = json.load(f)
        df = pd.DataFrame(raw_data)
    else:
        st.warning("No hazard data found. Please submit a report first.")
        df = pd.DataFrame()

    if not df.empty:
        df['reported_timestamp'] = pd.to_datetime(df['reported_timestamp'])
        
        st.markdown("###  Filter Active Reports")
        f1, f2 = st.columns(2)
        
        segments = ["All"] + sorted(df['trail_segment'].unique().tolist())
        filter_seg = f1.selectbox("Filter by Segment", segments)
        
        categories = ["All"] + sorted(df['hazard_type'].unique().tolist())
        filter_cat = f2.selectbox("Filter by Category", categories)
        
        filtered_df = df.copy()
        if filter_seg != "All":
            filtered_df = filtered_df[filtered_df['trail_segment'] == filter_seg]
        if filter_cat != "All":
            filtered_df = filtered_df[filtered_df['hazard_type'] == filter_cat]

        st.write(f"Showing {len(filtered_df)} reports based on your filters.")
        st.dataframe(
            filtered_df[['reported_timestamp', 'trail_segment', 'hazard_type', 'severity_rating', 'ai_description', 'recommended_action']],
            use_container_width=True,
            hide_index=True
        )
