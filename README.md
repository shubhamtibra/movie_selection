# How to use this code

This is a simple flask app in python to select movies for gives maximum profit.

To run this, first install flask using:
```
pip install flask
```
Then move the code directoy and run:
```
export FLASK_APP=run.py
flask run
```
The server will start.

Now go to the Postman Chrome Extension. Enter http://localhost:5000/submit in the URL section. Select Post as the type of the request.
Go to body and select Raw Json (application/json) as the body type.

In the body specify movie name, start date, end date in json format using example below.
```
{"Movie name":["Race", "Inception", "Get Out", "NO", "FRIENDS", "YES"],
"Start Date":["02 Feb", "04 Feb", "01 Feb", "06 Feb", "09 Feb", "06 Feb"], "End Date":["03 Feb", "05 Feb", "07 Feb", "08 Feb", "10 Feb", "10 Feb"]}
```
The maximum profit and movies selected will be returned in response.
