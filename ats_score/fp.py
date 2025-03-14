from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontpage.html')

@app.route('/ats-score')
def ats_score():
    return "ATS Score Analysis Page"

@app.route('/download')
def download():
    return "Download Application Page"

if __name__ == '__main__':
    app.run(debug=True,port=8080,use_reloader=False)
