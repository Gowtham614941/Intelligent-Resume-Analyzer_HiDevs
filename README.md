Intelligent Resume Analyzer
An intermediate-level Python project that simulates an Applicant Tracking System (ATS).  
The system analyzes resumes, matches candidates against job requirements, ranks them, and generates hiring recommendations.

Project Structure
intelligent-resume-analyzer/
│
├── main.py              # Entry point of the application
├── models.py            # Candidate data model (OOP)
├── matcher.py           # Scoring & ranking logic
├── reporter.py          # Report generation
├── utils.py             # Input validation utilities
├── resume_parser.py     # Resume parsing (Text/PDF/DOCX)
├── file_manager.py      # Save results to JSON
│
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files for Git


Features
- Accepts ob Details
  - Job Title
  - Required Skills
  - Required Experience
  - Required Degree

- Accepts Candidate Resume Input
  - Manual resume text entry
  - PDF resume parsing
  - DOCX resume parsing
  - TXT resume parsing

- Intelligent Candidate Evaluation
  - Skill matching
  - Experience scoring
  - Degree matching
  - Candidate ranking

- Generates Detailed Report
  - Candidate scores
  - Ranking
  - Hiring decision (Selected / Maybe / Rejected)

- JSON Export
  - Saves results to `results.json`
  - - Input Validation & Error Handling

Workflow
1. User enters **job requirements**
2. User inputs **number of candidates**
3. For each candidate:
   - Choose input type (Manual / PDF / DOCX / TXT)
   - Resume is parsed automatically
4. System evaluates each candidate using scoring logic
5. Candidates are ranked by match score
6. Hiring decision is generated
7. Results are saved in `results.json`


Scoring Method
Each candidate is scored out of **100+ points** based on:
1. Skill Matching
- Each matching skill → **+10 points**
- Compares candidate skills with job-required skills
2. Experience Score
- Each year of experience → **+5 points**
3. Degree Match
- If candidate degree matches required degree → **+20 points**
 4. Experience Requirement Bonus
- If candidate experience ≥ required experience → **+15 points**

Hiring Decision Logic
| Score Range | Decision |
|------------|----------|
| 70+        | Selected |
| 50 – 69    | Maybe    |
| < 50       | Rejected |


Requirements
Install dependencies:
bash
pip install -r requirements.txt

Required Libraries
* PyPDF2 → PDF parsing
* python-docx → DOCX parsing

How to Run
bash
python main.py

Example Output
* Ranked candidate list
* Match score
* Hiring decision
* JSON result file

Future Improvements
* NLP-based skill extraction
* Web application (Flask)
* GUI version (Tkinter)
* ATS-style scoring (0–100)
* Resume keyword analysis
* Charts & analytics

