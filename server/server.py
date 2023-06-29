from flask import Flask

AGENT_PORT=1111
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def main():
    return 'Hello Docker !!! '

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=AGENT_PORT, threaded=True, use_reloader=True, use_debugger=True)
    