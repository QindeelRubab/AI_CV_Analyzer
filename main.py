"""
AI CV Analyzer
A beginner-friendly terminal project that extracts text from a PDF CV,
cleans the text, detects listed skills, and saves a plain-text report.
"""

from pathlib import Path
import re
from PyPDF2 import PdfReader


# Add or edit skills here as you learn more technologies.
SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "SQL",
    "HTML",
    "TensorFlow",
    "CSS",
    "JavaScript",
    "React",
    "Django",
    "Flask",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Excel",
    "Git",
    "GitHub",
    "Linux",
    "Communication",
    "Problem Solving",
]


def extract_text_from_pdf(pdf_path):
    """Read a PDF file and return all extractable text as one string."""
    reader = PdfReader(str(pdf_path))
    pages_text = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        pages_text.append(page_text)

    return "\n".join(pages_text)


def clean_text(text):
    """Remove blank lines and repeated spaces while keeping words separated."""
    lines = text.split("\n")
    non_empty_lines = []

    for line in lines:
        cleaned_line = " ".join(line.split())
        if cleaned_line != "":
            non_empty_lines.append(cleaned_line)

    return " ".join(non_empty_lines)


def detect_skills(cv_text, skills=None):
    """Return skills mentioned in the CV, ignoring letter case."""
    if skills is None:
        skills = SKILLS

    searchable_text = cv_text.lower()
    found_skills = []

    for skill in skills:
        # Escape symbols such as + in C++ so they are treated literally.
        escaped_skill = re.escape(skill.lower())
        # Avoid matching a skill as part of a longer word.
        pattern = rf"(?<!\w){escaped_skill}(?!\w)"

        if re.search(pattern, searchable_text):
            found_skills.append(skill)

    return found_skills


def build_report(pdf_path, cleaned_text, found_skills):
    """Create the text content for the analysis report."""
    word_count = len(cleaned_text.split())

    report_lines = [
        "AI CV ANALYZER REPORT",
        "=" * 40,
        f"CV file: {Path(pdf_path).name}",
        f"Word count: {word_count}",
        "",
        "SKILLS FOUND",
        "-" * 40,
    ]

    if found_skills:
        report_lines.extend(f"- {skill}" for skill in found_skills)
    else:
        report_lines.append("No listed skills were detected.")

    report_lines.extend([
        "",
        "IMPORTANT NOTE",
        "-" * 40,
        "This beginner project checks for skill keywords only.",
        "It does not judge CV quality or guarantee job suitability.",
    ])

    return "\n".join(report_lines)


def analyze_cv(pdf_path):
    """Run extraction, cleaning, skill detection, and report creation."""
    path = Path(pdf_path).expanduser()

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError("Please provide a path to a PDF file, not a folder.")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The selected file must be a PDF (.pdf).")

    extracted_text = extract_text_from_pdf(path)

    if not extracted_text.strip():
        raise ValueError(
            "No readable text was found. This may be a scanned/image-only PDF. "
            "Try a text-based PDF for this version of the project."
        )

    cleaned_text = clean_text(extracted_text)
    found_skills = detect_skills(cleaned_text)
    report = build_report(path, cleaned_text, found_skills)

    report_path = path.with_name(f"{path.stem}_analysis_report.txt")
    report_path.write_text(report, encoding="utf-8")

    return cleaned_text, found_skills, report, report_path


def main():
    print("=" * 40)
    print("AI CV ANALYZER")
    print("=" * 40)
    print("This program extracts text from a PDF CV and checks for skill keywords.")
    print("Tip: You can enter a full path, or a path relative to this project folder.")
    print()

    pdf_path = input("Enter the path to your PDF CV: ").strip().strip('"')

    try:
        cleaned_text, found_skills, report, report_path = analyze_cv(pdf_path)

        print("\nANALYSIS COMPLETE")
        print("-" * 40)
        print(f"Words found: {len(cleaned_text.split())}")

        if found_skills:
            print("Skills detected:")
            for skill in found_skills:
                print(f"  - {skill}")
        else:
            print("No listed skills were detected.")

        print(f"\nFull report saved to:\n{report_path}")
        print("\n--- REPORT PREVIEW ---")
        print(report)

    except FileNotFoundError as error:
        print(f"\nError: {error}")
        print("Check the spelling and location of the file, then try again.")
    except ValueError as error:
        print(f"\nError: {error}")
    except Exception as error:
        print(f"\nSomething went wrong: {error}")
        print("If the problem continues, share the full error message for debugging.")


if __name__ == "__main__":
    main()
