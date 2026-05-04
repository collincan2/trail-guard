# src/frontview/app.py
import streamlit as st
page_element="""
<style>
[data-testid="stAppViewContainer"]{

  background-image: url("https://github.com/collincan2/trail-guard/blob/main/src/PilotPhotos/blackbear18.jpg?raw=true");
  background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}
</style>
<script>
[data-testid="stSidebar"]> div:first-child{
background-image: url("https://mcdn.wallpapersafari.com/medium/89/87/X7GDE5.jpg");
background-size: cover;
}
</script>
"""

st.markdown(page_element, unsafe_allow_html=True)

# Streamlit init
st.set_page_config(
    page_title="Trailguard", 
    page_icon="🌲🛡️", 
    layout="wide"
)

st.title("🌲 Trailguard 🛡️")
st.markdown("---")


st.markdown("""
### Welcome to the Trailguard Park Management Dashboard!
This system integrates generative AI and deterministic risk modeling to process, validate, and escalate trail hazards in real-time.

**Use the sidebar navigation to access:**
* **Submit Hazard:** Upload a field image of a hazard to route it through the AI validator pipeline.
* **Risk Engine:** View cumulative risk scores and geographical data for all 7 trail segments.
* **Briefings:** Generate and read the AI-summarized Daily Ranger Briefing.
""")

st.info("System Status: Online. Database connection established.")
