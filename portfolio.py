from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')
@app.route('/projects')
def success():
  return render_template('success.html')
@app.route('/about')
def about():
  return render_template('about.html')
app.run(debug=True)
