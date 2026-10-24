# AI CV Analyzer

A beginner-friendly Python terminal project that reads a text-based PDF CV, cleans the extracted text, detects skill keywords, and saves a text report.

## Features

- Extracts text from PDF files using PyPDF2.
- Cleans blank lines and repeated spaces.
- Detects skill keywords without case sensitivity.
- Handles common file/path errors.
- Saves a report beside the selected PDF.
- Includes basic automated tests for text cleaning and skill detection.

## Requirements

- Python 3.10 or newer
- pip
- A text-based PDF CV (image-only scanned PDFs are not supported by this version)

## Setup on Windows

Open the project folder in VS Code. In the VS Code terminal, run:

```powershell
python -m pip install -r requirements.txt
```

If you already have a virtual environment named `venv`, activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If activation does not work, you can still use the environment's Python directly:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main.py
```

Or, if you are not using a virtual environment:

```powershell
python main.py
```

## Run the program

```powershell
python main.py
```

When prompted, enter the full path to a PDF, for example:

```text
C:\Users\YourName\Documents\sample_cv.pdf
```

You can also put a test PDF in `cv_files` and enter:

```text
cv_files\sample_cv.pdf
```

The program prints the detected skills and saves a file named like `sample_cv_analysis_report.txt` next to the PDF.

## Run the tests

```powershell
python -m unittest discover -s tests -v
```

## Project structure

```text
AI_CV_Analyzer/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── cv_files/
│   └── (keep private CV PDFs here; do not upload them)
└── tests/
    └── test_main.py
```

## Current limitations

- This is a keyword-based analyzer, not a machine-learning model.
- It cannot read text from image-only scanned PDFs.
- It does not score candidates or decide whether someone should be hired.
- The skills list is editable in `main.py`.

## Privacy

Do not commit real CVs, phone numbers, addresses, email addresses, or generated reports containing personal information. The `.gitignore` file excludes PDFs inside `cv_files` and generated analysis reports.

## Future improvements

Possible next steps after this version works:
- Add more skills and aliases.
- Extract contact details carefully.
- Compare a CV against a job description.
- Add a simple user interface.
