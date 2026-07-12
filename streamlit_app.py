import streamlit as st
st.title("🤖 AI Resume Screener")
st.write("Upload your resume and job description to calculate ATS score.")
resume = st.file_uploader(
    "upload resume",
    type=["pdf"]
)
jd = st.text_area(
    "Job description",
    height = 250 ,
    placeholder = "Type Job Description "
)
analyze = st.button("🚀 Analyze Resume")
if analyze:
    st.write("Analyzing Resume...")
    if resume is None:
        st.error("Please upload your resume")
    elif job_description == "":
         st.error("Please Paste Job Description")
    else:
        st.success("Everything looks perfect ") 
    
          