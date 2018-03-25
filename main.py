from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def showmyip():
    if 'X-Forwarded-For' in request.headers.keys():
        source_ip = request.headers['X-Forwarded-For']
        return str(source_ip)
    else:
        source_ip = request.remote_addr
        return "No proxy header found, result may be inaccurate:" + str(source_ip)
