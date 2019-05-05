import flask 
import subprocess

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Docker Vuln Scanner</h1> \
    <p>This site runs a basic nmap scanner within a docker container</p>"

@app.route('/api/v1/Scan', methods=['GET'])
def scan_api():
    cmd = ["nmap","-v scanme.nmap.org"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/api/v1/files', methods=['GET'])
def files_api():
    cmd = ["ls","-a"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

app.run(host='0.0.0.0', port=80)