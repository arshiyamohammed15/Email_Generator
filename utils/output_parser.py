"""
Module: output_parser.py

Purpose:
Extract the email subject and body from the Gemini response.
"""


def parse_email(generated_email: str) -> tuple[str, str]:
    """
    Parse the generated email into Subject and Body.

    Args:
        generated_email (str): Response returned by Gemini.

    Returns:
        tuple:
            subject (str)
            body (str)
    """

    subject = ""
    body = ""

    lines = generated_email.splitlines()

    current_section = None
    body_lines = []

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower().startswith("subject:"):
            subject = stripped_line.replace("Subject:", "", 1).strip()
            current_section = None

        elif stripped_line.lower().startswith("body:"):
            current_section = "body"

        elif current_section == "body":
            body_lines.append(line)

    body = "\n".join(body_lines).strip()

    return subject, body