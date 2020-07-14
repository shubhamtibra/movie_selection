from flask import Flask, request, render_template, make_response, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
 return "Please use a /submit post request to give the movie data and the response will be returned in json"

@app.route('/submit', methods=['POST'])
def submit():
  data = request.get_json()
  sdate = data['Start Date']
  fdate = data['End Date']
  sdate = [datetime.strptime(date, "%d %b") for date in sdate]
  fdate = [datetime.strptime(date, "%d %b") for date in fdate]
  movies = list(zip(data['Movie name'], sdate, fdate))
  if(len(movies) == 0):
    return make_response(jsonify({}), 200)
  movies.sort(key=lambda x:x[2])
  selected = [movies[0][0]]
  i = 0
  for j in range(1, len(movies)):
    if movies[j][1] >= movies[i][2]:
        selected.append(movies[j][0])
        i=j

  res = {"Maximum Money" : '{} Crores'.format(len(selected)), "Selected Movies":selected}

  return make_response(jsonify(res), 200)
  #return 'You entered: {}'.format(request.get_json())

app.run(host="localhost", debug=True)