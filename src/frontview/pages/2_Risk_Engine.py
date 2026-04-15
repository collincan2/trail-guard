import streamlit as st
import pandas as pd
import json
import os
import sys

# Connect to the root folder
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from risk_engine import analyze_segment_risk

st.set_page_config(page_title="Risk Engine", layout="wide")
st.title(" Risk Engine & Hazard Database")

# Use tabs to cleanly separate the Live Engine from the Database view
tab1, tab2 = st.tabs(["Live Risk Analysis", "Hazard Database"])

with tab1:
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
                
                # Display metrics in a clean row
                m1, m2, m3 = st.columns(3)
                m1.metric("48-Hour Reports", data['reports_48h'])
                m2.metric("Location Multiplier", f"{data['multiplier']}x")
                
                # Highlight the risk score in red if it's over 10.0
                score_color = "normal" if data['risk_score'] < 10.0 else "inverse"
                m3.metric("Cumulative Risk Score", f"{data['risk_score']:.1f}", delta_color=score_color)

                st.markdown("---")
                
                # Show the AI Escalation Note if triggered
                if data['escalation_triggered']:
                    st.error("RISK ESCALATION TRIGGERD")
                    st.warning(f"**AI Dispatch Note:** {data['escalation_note']}")
                else:
                    st.success("Segment is currently operating within acceptable safety parameters.")


# --- TAB 2: Hazard Database Filter ---
with tab2:
    db_path = os.path.join(root_dir, "hazard_db.json")
    
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
