import re

def latex_to_string(latex_content):
    # Remove LaTeX commands like \textbf{}, \textit{}, etc.
    latex_content = re.sub(r'\\documentclass.*?\n', '', latex_content, flags=re.DOTALL)
    latex_content = re.sub(r'\\usepackage{.*?}', '', latex_content)
    latex_content = re.sub(r'\\begin{document}', '', latex_content)
    latex_content = re.sub(r'\\end{document}', '', latex_content)
    
    # Convert section headers
    latex_content = re.sub(r'\\section\*?\{(.+?)\}', r'\n\n### \1\n', latex_content)

    # Convert bold text
    latex_content = re.sub(r'\\textbf\{(.+?)\}', r'**\1**', latex_content)

    # Convert links
    latex_content = re.sub(r'\\href\{(.+?)\}\{(.+?)\}', r'\2: \1', latex_content)

    # Convert lists
    latex_content = re.sub(r'\\begin{itemize}', '', latex_content)
    latex_content = re.sub(r'\\end{itemize}', '', latex_content)
    latex_content = re.sub(r'\\item ', '- ', latex_content)

    # Remove any extra LaTeX formatting
    latex_content = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', latex_content)
    latex_content = re.sub(r'\\[a-zA-Z]+', '', latex_content)
    latex_content = re.sub(r' +', ' ', latex_content)  # Remove extra spaces

    return latex_content.strip()





latex_code =r'''
\documentclass{resume} 

\usepackage[left=0.4in,top=0.4in,right=0.4in,bottom=0.4in]{geometry} % Document margins
\newcommand{\tab}[1]{\hspace{.2667\textwidth}\rlap{#1}} 
\newcommand{\itab}[1]{\hspace{0em}\rlap{#1}}
\name{Subburaj S}
\address{<LOCATION>} 
\address{\href{mailto:<EMAIL>}{<EMAIL>} \\ \href{https://linkedin.com/in/subburaj-s-b22641100}{linkedin.com/in/subburaj-s-b22641100} \\ \href{https://<URL>}{<URL>}}

\begin{document}

%----------------------------------------------------------------------------------------
%	SUMMARY
%----------------------------------------------------------------------------------------

\begin{rSection}{SUMMARY}

Assistant Professor with 13+  years of experience successfully contributing to Computer Science curriculum development and delivery. 

Skilled in Python ,C, C++,Power BI, Microsoft Excel, SQL, Microsoft Word, and C#.

Driven to contribute to program outcomes by facilitating engagement and supporting learning objectives. Enthusiastic professional with background in academic advisement.

Established research agenda in Network Security and Machine learning field to publish in peer reviewed journals.

https://www.coursera.org/learner/subburajs

\end{rSection}

%----------------------------------------------------------------------------------------
%	EDUCATION SECTION
%----------------------------------------------------------------------------------------

\vspace{1.5em}

\begin{rSection}{Education}
{\bf B.Tech} Computer Science Engineering with AI\&ML, SRM University \hfill {Expected 2027}
\end{rSection}

\vspace{1.5em}

%----------------------------------------------------------------------------------------
%	SKILLS
%----------------------------------------------------------------------------------------

\begin{rSection}{SKILLS}

\begin{tabular}{@{}>{\bfseries}l @{\hspace{4ex}}p{0.75\textwidth} @{}}
Technical Skills & <GITHUB_LANGS>, Node.js, Deno, Bun, Supabase, MongoDB, Git\\
Design & Responsive, Best Practices, Industry Trends, Minimal, UX/UI\\
Frameworks & Next.js, ReactJS, Fresh, Express, FastAPI, Astro, SolidJS, TailwindCSS, Framer Motion\\
\end{tabular}

\end{rSection}

\vspace{1.5em}

%----------------------------------------------------------------------------------------
%	EXPERIENCE
%----------------------------------------------------------------------------------------

\begin{rSection}{EXPERIENCE}

\textbf{Assistant Professor (Sr.Gr)} \hfill Jun 2024 - Present\\
Amrita Vishwa Vidyapeetham \hfill \textit{Coimbatore, Tamil Nadu, India}

Teaching data science based subjects

\textbf{Assistant Professor} \hfill Jul 2022 - Jun 2024\\
SRM Institute of Science and Technology, Ramapuram \hfill \textit{Chennai, Tamil Nadu, India}

Faculty co ordinator for National level technical sympoisum Aurganon 23 and 24
Co Convenor for CyberHackathon 2024 colorabartion with Greater Chennai Police

\textbf{Assistant Professor} \hfill Jul 2015 - Jul 2022\\
Panimalar Engineering College \hfill \textit{Chennai Area, India}

Used variety of learning modalities and support materials to facilitate learning process and
accentuate presentations, including visual, aural and social learning modalities.

Helped struggling students by providing support outside of classrooms and consistently checking in
on progress.

Evaluated and supervised student activities and performance levels to provide reports on
academic progress.

Performed research to serve as basis for academic writing for publication.

Collaborated with faculty members on Funded projects.

Collaborated with colleagues on curriculum revision, evaluation of course syllabi and lesson
plans for Computer Science and Artificial intelligence curriculum. 

Mentored students and communicated internship and employment opportunities.

Facilitated academic and community collaborations to increase the number of community engaged research proposal submissions to extramural funders.

\textbf{Course Administrator for coursera} \hfill Apr 2020 - Jan 2021\\
Panimalar Engineering College \hfill \textit{Chennai, Tamil Nadu}

Organization Administrators (Org Admins) are admins who have full administrative rights to all programs within their organization's Coursera instance.

These  admins can add or remove other admins of their program at any time. Org Admins can:

Add learners to all learning programs
Remove learners from all learning programs
Access learner data in all learning programs

\textbf{Assistant Professor} \hfill Jun 2011 - May 2015\\
SRINIVASA INSTITUTE OF ENGG & TECH \hfill \textit{CHENNAI}

Helped struggling students by providing support outside of classrooms and consistently checking in
on progress.
Used variety of learning modalities and support materials to facilitate learning process and
accentuate presentations, including visual, aural and social learning modalities.


\end{rSection}

\vspace{1.5em}

%----------------------------------------------------------------------------------------
%	PROJECTS
%----------------------------------------------------------------------------------------

\begin{rSection}{PROJECTS}    
    \item \textbf{\href{https://github.com/AksayaVenugopal/Voice-Code-Complier}{Voice-Code-Complier}}\\
Stars: 0\\
Description: Created a Voice Code Compiler using Natural Language Processing, integrating SpeechRecognition and PyAutoGUI to execute code based on voice input with 85% accuracy. Emphasized modularity and error-handling to improve usability.
\\
\item \textbf{\href{https://github.com/AksayaVenugopal/Image-Caption-Generator}{Image-Caption-Generator}}\\
Stars: 0\\
Description:  Developed an AI-powered image caption generator using a CNN for feature extraction and an LSTM model for
captions, achieving 72.57% accuracy. Utilized scalable data processing to handle large datasets and optimize
performance.
\\
\item \textbf{\href{https://github.com/AksayaVenugopal/Movie-review-API}{Movie-review-API}}\\
Stars: 0\\
Description:  Built a movie review platform using Java, Spring Boot, React, and MongoDB. Emphasized user authentication, data
integrity, and scalability across components.
\\

\end{rSection}
\vspace{1.5em}

%----------------------------------------------------------------------------------------
%	LANGUAGES
%----------------------------------------------------------------------------------------

\begin{rSection}{LANGUAGES}

\begin{itemize}
    English (), Tamil (), Telugu ()
\end{itemize}

\end{rSection}



%----------------------------------------------------------------------------------------
%	CERTIFICATIONS
%----------------------------------------------------------------------------------------

\begin{rSection}{CERTIFICATIONS}

    \begin{itemize}
        Chatbot Building Essentials, IBM Applied AI Specialization, Deep learning specialization,  Coursera Administrator Training,  Convolutional Neural Networks in TensorFlow, Crash Course on Python, Building Deep Learning Applications with Keras 2.0, PyTorch Essential Training: Deep Learning, OpenCV for Python Developers, Deep Learning: Face Recognition, Deep Learning Fundamentals, Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning, Learning Python with PyCharm, Introduction to Internet of Things, Design and Analysis of Algorithms, OPERATING SYSTEM, EMC ACADAMIC ASSOCIATE, INTRODUCTION TO CRYPTOLOGY, micorosoft certified professional
    \end{itemize}
    
    \end{rSection}
    

%----------------------------------------------------------------------------------------
%	EXTRA-CURRICULAR ACTIVITIES
%----------------------------------------------------------------------------------------

\begin{rSection}{EXTRA-CURRICULAR ACTIVITIES}

    \begin{itemize}
        \item Actively writing blog posts in social media like \href{https://www.linkedin.com/in/rahul-marban}{LinkedIn}, viewed by over 10K+ people.
        \item Participated in 4+ hackathons and coding competitions.
        \item Contributed and Developed various (30+) open-source projects
    \end{itemize}
    
    \end{rSection}
    
    \vspace{1.5em}

    
    \end{document}
'''
# Convert to plain text
plain_text = latex_to_string(latex_code)
print(plain_text)
