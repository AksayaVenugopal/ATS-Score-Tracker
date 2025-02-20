![image](https://github.com/user-attachments/assets/04cdd5b8-93be-4bbc-9914-aece386e1ae9)

Automated Resume ATS Scoring System
Overview
This project is a Flask-based web application that evaluates resumes against job descriptions using an ATS (Applicant Tracking System) scoring algorithm. The system extracts key information from a LaTeX-based resume, compares it with job requirements, and assigns scores based on content, formatting, skills, and style. The application also identifies missing skills and sections to improve resume alignment with job postings.

Features
Content Analysis: Evaluates the quality of resume content, including repetition, spelling, grammar, and impact metrics.
Formatting Evaluation: Assesses the structure, bullet points, section completeness, and length.
Skills Matching: Compares resume skills with job requirements and balances hard and soft skills.
Style Assessment: Detects passive voice, email presence, and buzzwords.
Missing Skills & Sections Identification: Highlights areas for improvement.
REST API Support: Provides ATS scores as JSON responses.
Requirements
Dependencies
Ensure you have the following installed:

Python 3.x
Flask
Pandas
Scikit-learn
OpenPyXL
Install required packages using:

sh
Copy
Edit
pip install flask pandas scikit-learn openpyxl
File Structure
graphql
Copy
Edit
.
├── app.py                  # Main Flask application
├── templates
│   ├── frontpage.html      # Homepage
│   ├── index.html          # ATS Score input page
├── skillsdataset
│   ├── skills_dataset.xlsx # Skills dataset
│   ├── skills_dataset1.xlsx # Known phrases dataset
│   ├── skills_dataset2.xlsx # Soft skills dataset
Running the Application
Clone the repository and navigate to the project directory.
sh
Copy
Edit
git clone <repository_url>
cd <project_directory>
Run the Flask application:
sh
Copy
Edit
python app.py
Open a browser and visit:
cpp
Copy
Edit
http://127.0.0.1:8080/
API Usage
Endpoint: /ats-score
Method: POST
Request Parameters:
resume (String): LaTeX code of the resume.
job_description (String): Text-based job description.
Example Request:
json
Copy
Edit
{
  "resume": "LaTeX resume content here",
  "job_description": "Job description content here"
}
Example Response:
json
Copy
Edit
{
  "Content Score": 20.5,
  "Formatting Score": 22.0,
  "Skills Score": 24.0,
  "Style Score": 23.5,
  "Missing Skills": ["Python", "Machine Learning"],
  "Missing Sections": ["Experience"],
  "ATS Score": 90.0
}
Customization
Update the skills_dataset.xlsx, skills_dataset1.xlsx, and skills_dataset2.xlsx files to modify skill matching.
Adjust regex patterns and weightings in calculate_ats_score() to refine scoring logic.
Conclusion
This ATS scoring system provides insights into resume optimization for job applications. Modify datasets and scoring logic as needed to align with industry requirements.
