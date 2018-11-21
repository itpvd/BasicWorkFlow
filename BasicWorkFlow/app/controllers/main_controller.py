from flask import Flask, render_template, request, json
from app import app
from app.model.check import Check
from app.model.loop import Loop

@app.route('/')
@app.route('/workflowpage')
def workflowpage():
    return render_template('workflow.html')

@app.route('/workflow', methods=['POST'])
def hello_world3(name=None):
    try:
        input = request.form
        lists = input['listnumber'].split(" ")
        listnumber=[int(x) for x in lists]
        result = Loop.loop(int(input['numberloop']),Check.check(listnumber))
        result['status']='200'
        return json.dumps(result);
    except Exception as exception:
        return json.dumps({'error':type(exception).__name__});
   
