import flask 
import subprocess
import subprocess
import shlex
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Docker Vuln Scanner</h1> \
    <p>This site runs a basic nmap scanner within a docker container</p>"

@app.route('/api/v1/Scan', methods=['GET'])
def execute():
    print("============")
    if 'ip' in request.args:
        command = 'nmap -sV '
        ip = request.args['ip']
        command = command + ip
        command = command + ' --script vulners.nse -oX out.xml'
        print(command)
    if request.method == 'GET':
        print('Started executing command')
        command = shlex.split(command)
        process = subprocess.Popen(command, stdout = subprocess.PIPE)
        print("Run successfully")
        output, err = process.communicate()
        return output
    return "not executed"

@app.route('/api/v1/files', methods=['GET'])
def files_api():
    command = "ls -a"
    print(command)
    if request.method == 'GET':
        print('Started executing command')
        command = shlex.split(command)
        print('split command')
        process = subprocess.Popen(command, stdout = subprocess.PIPE)
        print("Run successfully")
        output, err = process.communicate()
        return output
    return "not executed"

@app.route('/api/v1/lastScan', methods=['GET'])
def lastscan_api():
    command = "cat out.xml"
    print(command)
    if request.method == 'GET':
        print('Started executing command')
        command = shlex.split(command)
        print('split command')
        process = subprocess.Popen(command, stdout = subprocess.PIPE)
        print("Run successfully")
        output, err = process.communicate()
        return output
    return "not executed"

app.run(host='0.0.0.0', port=80)