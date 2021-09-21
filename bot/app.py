'''from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":'''

from flask import Flask, redirect, url_for, request, render_template
import requests
import json

app = Flask(__name__, template_folder= 'Templates')
context_set = ""

@app.route('/bot', methods = ['POST', 'GET'])
def index():

    query=""
    if request.method == 'GET':
        query = str(request.args.get('text'))
        data = json.dumps({"sender": "Rasa","message": query})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()
        query = res[0]['text']
    return render_template('index.html', val=query)

if __name__ == '__main__':
    app.run(debug=True)