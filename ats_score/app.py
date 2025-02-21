from flask import Flask, render_template, request, jsonify
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
def calculate_ats_score(job_description,resume_latex,skills_list,known_phrases,soft_skills):
    job_skills = set(skill for skill in skills_list if re.search(rf'\b{re.escape(skill)}\b', job_description, re.IGNORECASE))
    
    
    latex_content = re.sub(r'\\documentclass.*?\n', '', resume_latex, flags=re.DOTALL)
    latex_content = re.sub(r'\\usepackage{.*?}', '', latex_content)
    latex_content = re.sub(r'\\begin{document}', '', latex_content)
    latex_content = re.sub(r'\\end{document}', '', latex_content)
    latex_content = re.sub(r'\\section\*?\{(.+?)\}', r'\n\n### \1\n', latex_content)
    latex_content = re.sub(r'\\textbf\{(.+?)\}', r'**\1**', latex_content)
    latex_content = re.sub(r'\\href\{(.+?)\}\{(.+?)\}', r'\2: \1', latex_content)
    latex_content = re.sub(r'\\begin{itemize}', '', latex_content)
    latex_content = re.sub(r'\\end{itemize}', '', latex_content)
    latex_content = re.sub(r'\\item ', '- ', latex_content)
    latex_content = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', latex_content)
    latex_content = re.sub(r'\\[a-zA-Z]+', '', latex_content)
    latex_content = re.sub(r' +', ' ', latex_content)  
    latex_content = latex_content.strip()

    cleaned_text = re.sub(r'\\[a-zA-Z]+\*?(?:\{.*?\})?', '', latex_content)    
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    
    for phrase in known_phrases:
        cleaned_text = re.sub(rf'\b{re.escape(phrase)}\b', phrase.replace(' ', '_'), cleaned_text, flags=re.IGNORECASE)    

    
    words = cleaned_text.split()    
    words = [word.replace('_', ' ') for word in words]
    resume_skills1 = words
    resume_skills = set(skill for skill in skills_list if any(re.search(rf'\b{re.escape(skill)}\b', desc, re.IGNORECASE) for desc in resume_skills1))
    
    
    content_score = 0
    formatting_score = 0
    skills_score = 0
    style_score = 0
    
    matched_skills = resume_skills & job_skills
    skills_score = (len(matched_skills) / len(job_skills)) * 70 
    
    
    word_counts = {word: cleaned_text.count(word) for word in words}
    repetition_penalty = sum(count > 1 for count in word_counts.values()) * 5  
    content_score += max(0, 100 - repetition_penalty)
    
    
    spelling_errors = len(re.findall(r'\b\w+\b', cleaned_text)) 
    grammar_penalty = 0 
    content_score += 100 - (spelling_errors * 0.1 + grammar_penalty)
    
    ]
    impact_count = len(re.findall(r'\d+%?', latex_content))
    impact_score = min(impact_count * 10, 30) 
    content_score += impact_score
    word_count = len(cleaned_text.split())
    if word_count < 500 or word_count > 2000:
        formatting_score -= 10 
    
    
    long_bullets = len(re.findall(r'- .{80,}', latex_content)) 
    formatting_score -= long_bullets * 5
    
    
    hard_skills = [skill for skill in resume_skills if skill in skills_list]
    soft_skills = [skill for skill in resume_skills if skill in soft_skills]
    
    skills_score += len(hard_skills) * 0.5 + len(soft_skills) * 0.5

    missing_sections = []
    if not re.search(r'\\section\*?\{Experience\}', resume_latex):
        missing_sections.append('Experience')
    if not re.search(r'\\section\*?\{Education\}', resume_latex):
        missing_sections.append('Education')
    
    
    email_found = bool(re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', latex_content))
    style_score += 10 if email_found else 0
    
    
    passive_voice_found = bool(re.search(r'\b(is|was|were|been|be)\s+[a-z]+ed\b', latex_content))
    style_score -= 10 if passive_voice_found else 0
    
    
    buzzwords = ['team player', 'hardworking', 'go-getter']
    buzzword_penalty = sum(1 for word in buzzwords if word in latex_content.lower()) * 5
    style_score -= buzzword_penalty
    
    
    ats_score = content_score + formatting_score + skills_score + style_score
    if formatting_score<0:
        formatting_score=0
    missing_skills = set(job_skills) - resume_skills
    #missing_sections += missing_skills
    print('Content Score',content_score,
        'Formatting Score', formatting_score,
        'Skills Score', skills_score,
        'Style Score', style_score,
        'Missing Skills', missing_skills,
        'Missing Sections', missing_sections,
        'ATS Score', ats_score)
    return  content_score, formatting_score,skills_score,style_score,missing_skills,missing_sections,ats_score
    
@app.route('/')
def home():
    return render_template('frontpage.html')


@app.route('/ats-score', methods=["GET", "POST"])
def ats_score():
    skills_df = pd.read_excel(r"D:\auto_resume\ats_score\skillsdataset\skills_dataset.xlsx", engine="openpyxl")
    skills_list = skills_df['Skills'].dropna().str.lower().tolist()
    soft_df = pd.read_excel(r"D:\auto_resume\ats_score\skillsdataset\skills_dataset2.xlsx", engine="openpyxl")
    soft_list = soft_df['Soft Skills'].dropna().str.lower().tolist()
    df1 = pd.read_excel(r"D:\auto_resume\ats_score\skillsdataset\skills_dataset1.xlsx")
    known_phrases = df1['known_phrases'].dropna().tolist()
    if request.method == "POST":
        latex_code = request.form.get("resume")
        job_description = request.form.get("job_description")
        if not latex_code or not job_description:
            return jsonify({"error": "Both resume and job description are required!"}), 400

        
        c,f,s,s1,m,m1,a = calculate_ats_score( job_description,latex_code,skills_list,known_phrases,soft_list)
        
        return jsonify({
        'Content Score': c,
        'Formatting Score': f,
        'Skills Score': s,
        'Style Score': s1,
        'Missing Skills': list(m),
        'Missing Sections':list(m1),
        'ATS Score': a
        })
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
