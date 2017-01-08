from flask import Flask, render_template, request
from os import environ

app = Flask(__name__)

#these are decorators
@app.route("/") # the argument is the URL endpoint
@app.route("/hello")
def say_hi(): # this function will be run at either endpoint (decorated by route)
    print(request.url)
    return render_template('template.html', url = request.url, name = None)
    
@app.route("/hello/<n>")
def say_hi_again(n):
    return render_template('template.html', url = request.url, name = n.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi = (last[0:3] + first[0:2]).title();
    return render_template('template.html', url = request.url, name = jedi, jedi = True)
    
#when you don't specify what type of data you return, Flask assumes that you are sending HTML

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))