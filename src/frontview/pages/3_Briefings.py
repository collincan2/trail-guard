# src/frontview/pages/3_Briefings.py
import streamlit as st
import os
import glob
import sys

# Connect to the root folder
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from briefing_engine import generate_daily_briefing

st.set_page_config(page_title="Ranger Briefings", page_icon="📋")
st.title(" Daily Ranger Briefings")
st.markdown("Generate and review AI-aggregated dispatch priorities.")

# Add a button to generate a new briefing from the UI
if st.button("🔄 Generate Today's Briefing Now"):
    with st.spinner("Compiling park-wide data and writing briefing..."):
        success, result = generate_daily_briefing()
        if success:
            st.success(f"Generated new briefing: {result}")
        else:
            st.error(result)

st.markdown("---")

# 3_briefings will look for .txt files in the root directory.
briefing_files = glob.glob("daily_briefing_*.txt")
briefing_files.sort(reverse=True) 

if not briefing_files:
    st.info("No daily briefings found. Click the button above to generate one!")
else:
    selected_file = st.selectbox("Select Briefing Date:", briefing_files)
    
    if selected_file:
        with open(selected_file, "r", encoding="utf-8") as f:
            briefing_content = f.read()
            
        st.markdown(briefing_content)
