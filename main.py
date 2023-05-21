from  flask import Flask as fl

app = fl(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

if __name__ == '__main__':
    host = "127.0.0.1"
    port = "5000"
    debug = False
    options = None
    app.run(host, port, debug, options)