from flask import Flask as fl 
from flask import render_template
import jinja2 as jj

# FLASK
app = fl(__name__)

def start_page():
    return render_template("test.html")
    # return '<p>Start Page</p>'

def hello_world():
    return '<p>Hello, World!</p>'

def input_page(url):
    return "This is the url you added: %s" % url

def table_page():
    cr = ["Quick", "Light", "Easy to use"]
    er = ["Latency", "Speed", "Size", "Cost"]
    return render_template("table_var.html", 
                           customer_requirements=cr,
                           engineering_requirements=er)
    
def shapes_page():
    return render_template("shapes.html")

if __name__ == '__main__':
    host = "127.0.0.1"
    port = "5000"
    debug = False
    options = None
    
    # Routing 
    app.add_url_rule('/hello', 'hello', hello_world)
    app.add_url_rule('/', 'start', start_page)
    app.add_url_rule('/table', 'table', table_page)
    app.add_url_rule('/shapes', 'shapes', shapes_page)
    
    app.add_url_rule('/<url>', 'input', input_page)
    
    
    # Start the server 
    app.run(host, port, debug, options) 
    