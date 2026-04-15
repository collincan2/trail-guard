# src/frontview/pages/1_Submit_Hazard.py
import streamlit as st
import datetime

st.set_page_config(page_title="Submit Hazard")

st.title("Upload Field Report")
st.markdown("Submit a new hazard image for AI categorization and severity scoring.")

# Build the input form
with st.form("hazard_submission_form"):
    uploaded_file = st.file_uploader("Select Hazard Image", type=["jpg", "jpeg", "png"])
    
    col1, col2 = st.columns(2)
    with col1:
        segment = st.selectbox("Trail Segment", [1, 2, 3, 4, 5, 6, 7])
    with col2:
        # Defaults to the current date/time for the 48-hour calculation logic
        report_time = st.text_input("Timestamp", value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        
    user_desc = st.text_area("Ranger Notes (Optional)")
    
    # The submit button
    submitted = st.form_submit_button("Run AI Analysis")

if submitted:
    if uploaded_file is not None:
        # UI Feedback
        with st.spinner("Analyzing image and validating JSON schema..."):
            
            # TO-DO import your analysis logic here, pass in the uploaded_file 
            # and save it to hazard_db.json under 'hazard_type'
            
            st.success(f"Report successfully validated and saved to database for Segment {segment}!")
    else:
        st.error("Please upload an image to proceed.")
