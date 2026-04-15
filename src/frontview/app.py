# src/frontview/app.py
import streamlit as st

# Streamlit init
st.set_page_config(
    page_title="Trailguard", 
    page_icon="🌲", 
    layout="wide"
)

st.title("🌲 Trailguard Operating System")
st.markdown("---")

st.markdown("""
### Welcome to the Park Management Dashboard
This system integrates generative AI and deterministic risk modeling to process, validate, and escalate trail hazards in real-time.

**Use the sidebar navigation to access:**
* **Submit Hazard:** Upload a field image to route it through the AI validator pipeline.
* **Risk Engine:** View cumulative risk scores and geographical data for all 7 trail segments.
* **Briefings:** Generate and read the AI-summarized Daily Ranger Briefing.
""")

st.info("System Status: Online. Database connection established.")
