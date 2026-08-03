import os
from dotenv import load_dotenv

load_dotenv()


def validate_resume(uploaded_resume):
    if uploaded_resume is None:
        raise ValueError("Please upload your resume.")

    if uploaded_resume.type != "application/pdf":
        raise ValueError("Only PDF files are supported.")


def validate_job_description(job_description: str):
    if not job_description:
        raise ValueError("Please enter the Job Description.")

    if not job_description.strip():
        raise ValueError("Job Description cannot be empty.")


def validate_api_key():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. Please configure your .env file."
        )


def validate_generated_email(email: str):
    if not email:
        raise ValueError("Gemini returned an empty response.")

    if not email.strip():
        raise ValueError("Generated email is empty.")