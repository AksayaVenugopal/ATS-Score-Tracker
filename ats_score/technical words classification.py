import re

# Function to convert LaTeX resume to plain text using regex
def latex_to_text_with_regex(latex_text):
    # Remove LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\*?{.*?}', '', latex_text)  # Remove commands like \textbf, \emph, etc.
    text = re.sub(r'\\[a-zA-Z]+', '', text)  # Remove simple LaTeX commands like \name, \address, etc.
    text = re.sub(r'\{.*?\}', '', text)  # Remove content inside braces (LaTeX arguments)
    
    # Remove inline math expressions (content between $...$)
    text = re.sub(r'\$.*?\$', '', text)
    
    # Remove block math expressions (content between \[...\])
    text = re.sub(r'\\\[.*?\\\]', '', text)
    
    # Remove special LaTeX symbols (like \%, \$, \&)
    text = re.sub(r'\\[%&$#_{}]', '', text)
    
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# Example LaTeX resume text
resume_latex = """
\\documentclass{resume} 
\\usepackage[left=0.4in,top=0.4in,right=0.4in,bottom=0.4in]{geometry} % Document margins
\\newcommand{\\tab}[1]{\\hspace{.2667\\textwidth}\\rlap{#1}} 
\\newcommand{\\itab}[1]{\\hspace{0em}\\rlap{#1}}
\\name{Subburaj S}
\\address{<LOCATION>} 
\\address{\\href{mailto:<EMAIL>}{<EMAIL>} \\\\ \\href{https://linkedin.com/in/subburaj-s-b22641100}{linkedin.com/in/subburaj-s-b22641100} \\\\ \\href{https://<URL>}{<URL>}}

\\begin{document}

\\begin{rSection}{SUMMARY}
Assistant Professor with 13+ years of experience successfully contributing to Computer Science curriculum development and delivery. 
Skilled in Python, C, C++, Power BI, Microsoft Excel, SQL, Microsoft Word, and C#.
\\end{rSection}

\\begin{rSection}{SKILLS}
Technical Skills & <GITHUB_LANGS>, Node.js, Deno, Bun, Supabase, MongoDB, Git\\
Design & Responsive, Best Practices, Industry Trends, Minimal, UX/UI\\
Frameworks & Next.js, ReactJS, Fresh, Express, FastAPI, Astro, SolidJS, TailwindCSS, Framer Motion\\
\\end{rSection}

\\begin{rSection}{EXPERIENCE}
Assistant Professor (Sr.Gr) \\\\
Teaching data science based subjects \\\\
Assistant Professor (July 2022 - Present) \\\\
Collaborated with faculty on Funded projects\\
\\end{rSection}

\\end{document}
"""

# Convert LaTeX resume to plain text using regex
resume_text = latex_to_text_with_regex(resume_latex)

# Print the extracted plain text
print(resume_text)
