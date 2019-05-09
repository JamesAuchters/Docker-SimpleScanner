from flask import Flask
from flask import request
import os
import subprocess
import shlex

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Docker Vuln Scanner</h1> \
    <p>This site runs a basic nmap scanner within a docker container - Flask presents an extremely dumb API for running ANY command & nmap commands</p> \
    <p>Use /Scan/?ip=demo or /Command/?command=ls to make things work!"

@app.route("/scan/",methods = ['GET'])
def runscan():
    command = "nmap -v "
    print("============")
    if 'option' in request.args:
        option = request.args['option']
        command = command + '-' + option + ' '
    if 'ip' in request.args:
        ip = request.args['ip']
        command = command + ip
        arguments = shlex.split(command)
        execution = subprocess.check_output(arguments)
        return execution
    
@app.route("/command/",methods = ['GET'])
def runcmds():
    if 'command' in request.args:
        command = request.args['command']
        arguments = shlex.split(command)
        execution = subprocess.check_output(arguments)
        return execution

app.run(host='0.0.0.0', port=80)