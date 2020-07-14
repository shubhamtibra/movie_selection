from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
  data = request.get_json()
  movies = data['Movie Name']
  sdate = data['Start Date']
  fdate = data['End Date']
  return 'You entered: {}'.format(request.get_json())

app.run(host="localhost", debug=True)