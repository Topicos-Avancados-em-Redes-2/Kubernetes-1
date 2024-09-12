from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Simula carga de CPU por alguns segundos
    time.sleep(1)
    return "Estressando"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
