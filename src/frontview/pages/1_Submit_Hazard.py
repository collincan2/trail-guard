import streamlit as st
import datetime
import sys
import os

# Get current folder (pages)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Climb up exactly TWO levels to hit the 'src' folder
src_dir = os.path.abspath(os.path.join(current_dir, "../../")) 

# Add it to the system path
if src_dir not in sys.path:
    sys.path.append(src_dir)

from analysis import analyze_hazard_image

st.set_page_config(page_title="Submit Hazard")
st.title("📸 Upload Field Report")
st.markdown("Submit a new hazard image for AI categorization and severity scoring.")

# Build the input form
with st.form("hazard_submission_form"):
    uploaded_file = st.file_uploader("Select Hazard Image", type=["jpg", "jpeg", "png"])
    
    col1, col2 = st.columns(2)
    with col1:
        segment = st.selectbox("Trail Segment", [1, 2, 3, 4, 5, 6, 7])
    with col2:
        # Default to exactly the YYYY-MM-DD HH:MM format
        report_time = st.text_input("Timestamp", value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        
    user_desc = st.text_area("Ranger Notes (Optional)")
    submitted = st.form_submit_button("Run AI Analysis")

# When the user clicks the button
if submitted:
    if uploaded_file is not None:
        with st.spinner("Analyzing image and validating JSON schema..."):
            
            # 2. Fire the engine! Pass the web inputs into your backend logic.
            success, result = analyze_hazard_image(
                image_input=uploaded_file, 
                segment_id=segment, 
                timestamp=report_time, 
                description=user_desc
            )
            
            if success:
                st.success(f"Report validated and saved to database for Segment {segment}!")
                
                # Expandable box to show the user the JSON the AI generated
                with st.expander("View Generated JSON Report"):
                    st.json(result)
            else:
                st.error(f"Pipeline Failed: {result}")
    else:
        st.warning("Please upload an image to proceed.")
