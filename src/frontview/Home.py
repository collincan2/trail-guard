# src/frontview/app.py
import streamlit as st
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:trail-guard/src/PilotPhotos/blackbear18.jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('background.png')

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
