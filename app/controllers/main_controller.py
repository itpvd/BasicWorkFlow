from flask import Flask, render_template, request, json
from app import app
from app.libs.loop_start import LoopStart
import app.configs.constant as const

#workflow page
@app.route('/')
@app.route('/workflowpage')
def workflowpage():
    return render_template('workflow.html')

#handle workflow
@app.route('/workflow', methods=['POST'])
def workflow():
    try:
        input = request.form
        lists = input['listnumber'].split(" ")
        numberloop=int(input['numberloop'])
        listnumber=[int(x) for x in lists]
        result = LoopStart.loopStart(numberloop,listnumber)
        result['status']=const.STATUS_OK
        return json.dumps(result);
    except Exception as exception:
        return json.dumps({'error':type(exception).__name__});
   