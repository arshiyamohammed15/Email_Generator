import streamlit as st
from utils.pdf_reader import extract_text
from utils.prompt_builder import build_prompt
from utils.gemini_client import generate_email

def validate_inputs(uploaded_resume, job_description):
    """
    Validate required user inputs before proceeding.
    Returns:
        (bool, str): (is_valid, error_message)
    """

    if uploaded_resume is None:
        return False, "Please upload your resume in PDF format."

    if uploaded_resume.type != "application/pdf":
        return False, "Only PDF files are supported."

    if not job_description.strip():
        return False, "Please enter the Job Description."

    return True, ""


def main():
    st.set_page_config(
        page_title="AI Job Application Email Generator",
        page_icon="📧",
        layout="centered",
    )

    st.title("📧 AI Job Application Email Generator")

    st.write(
        """
        Upload your resume and paste the job description.
        Click **Generate Email** to continue.
        """
    )

    # -----------------------------
    # Resume Upload
    # -----------------------------
    uploaded_resume = st.file_uploader(
        label="Upload Resume (PDF)",
        type=["pdf"],
        accept_multiple_files=False,
        help="Only PDF resumes are supported.",
    )

    # -----------------------------
    # Job Description Input
    # -----------------------------
    job_description = st.text_area(
        label="Paste Job Description",
        height=250,
        placeholder="Paste the complete Job Description here...",
    )

    # -----------------------------
    # Generate Button
    # -----------------------------
    generate_clicked = st.button(
        "Generate Email",
        use_container_width=True,
    )

    # -----------------------------
    # Validation
    # -----------------------------
    if generate_clicked:

        is_valid, error_message = validate_inputs(
            uploaded_resume,
            job_description,
        )

        if not is_valid:
            st.error(error_message)
            st.stop()

        # Temporary success message.
        # Future tasks will continue from here.
        try:
         resume_text = extract_text(uploaded_resume)

         prompt = build_prompt(
             resume_text=resume_text,
             job_description=job_description,
         )
     
         generated_email = generate_email(prompt)
     
         st.session_state["uploaded_resume"] = uploaded_resume
         st.session_state["job_description"] = job_description
         st.session_state["resume_text"] = resume_text
         st.session_state["prompt"] = prompt
         st.session_state["generated_email"] = generated_email
     
         st.success("Email generated successfully.")
         st.subheader("Generated Email")

         st.text_area(
          "Generated Email",
           value=generated_email,
           height=350,
          )

        except ValueError as error:
         st.error(str(error)) 
        

if __name__ == "__main__":
    main()