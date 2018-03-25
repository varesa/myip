from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def showmyip():
    ip = request.remote_addr
    return str(ip)
