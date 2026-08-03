"""
Module: prompt_builder.py

Purpose:
Build a structured prompt for Gemini using:
- Resume Text
- Job Description
- Email Generation Instructions
"""


def build_prompt(resume_text: str, job_description: str) -> str:
    """
    Build a structured prompt for Gemini.

    Args:
        resume_text (str): Extracted text from the resume.
        job_description (str): User-provided job description.

    Returns:
        str: Complete prompt string.
    """

    prompt = f"""
You are an AI assistant that generates professional job application emails.

Using the candidate's resume and the job description below, generate a professional job application email.

Resume:
{resume_text}

Job Description:
{job_description}

Instructions:
- Write a professional job application email.
- Include an appropriate email subject.
- Keep the tone formal and concise.
- Highlight relevant skills and experience from the resume.
- Tailor the email to the provided job description.
- Do not invent qualifications or experience that are not present in the resume.

Return ONLY in the following format.

Subject:
<Email Subject>

Body:
<Professional Email Body>

Do not copy slogans, taglines, or marketing phrases from the job description as the email opening or subject unless they are directly relevant.
"""

    return prompt.strip()