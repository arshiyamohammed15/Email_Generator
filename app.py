import streamlit as st

from utils.pdf_reader import extract_text
from utils.prompt_builder import build_prompt
from utils.gemini_client import generate_email
from utils.output_parser import parse_email
from utils.validator import (
    validate_resume,
    validate_job_description,
    validate_api_key,
    validate_generated_email,
)


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

        Click **Generate Email** to create a personalized job application email.
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
    # Validation & Email Generation
    # -----------------------------
    if generate_clicked:

        try:
            # -----------------------------
            # Validate User Inputs
            # -----------------------------
            validate_resume(uploaded_resume)
            validate_job_description(job_description)
            validate_api_key()

            # -----------------------------
            # Generate Email
            # -----------------------------
            with st.spinner("Generating personalized email..."):

                # Extract Resume Text
                try:
                    resume_text = extract_text(uploaded_resume)
                except Exception:
                    raise ValueError(
                        "Unable to extract text from the uploaded PDF."
                    )

                # Build Prompt
                prompt = build_prompt(
                    resume_text=resume_text,
                    job_description=job_description,
                )

                # Generate Email
                try:
                 generated_email = generate_email(prompt)
                except Exception as error:
                 raise ValueError(
                   f"Failed to generate email using Gemini.\n{error}"
                 )

                # Validate Gemini Response
                validate_generated_email(generated_email)

                # Parse Email
                subject, body = parse_email(generated_email)

                # -----------------------------
                # Store Session State
                # -----------------------------
                st.session_state["uploaded_resume"] = uploaded_resume
                st.session_state["job_description"] = job_description
                st.session_state["resume_text"] = resume_text
                st.session_state["prompt"] = prompt
                st.session_state["generated_email"] = generated_email
                st.session_state["email_subject"] = subject
                st.session_state["email_body"] = body

            # -----------------------------
            # Display Output
            # -----------------------------
            st.success("✅ Email generated successfully.")

            st.divider()

            with st.container(border=True):
                st.subheader("📧 Email Subject")

                st.text_input(
                    label="Subject",
                    value=subject,
                )

            with st.container(border=True):
                st.subheader("📝 Email Body")

                st.text_area(
                    label="Body",
                    value=body,
                    height=450,
                )

        except ValueError as error:
            st.error(str(error))

        except Exception:
            st.error(
                "An unexpected error occurred. Please try again."
            )


if __name__ == "__main__":
    main()