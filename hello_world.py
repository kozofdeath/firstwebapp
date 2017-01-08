from flask import Flask
from os import environ

app = Flask(__name__)

#these are decorators
@app.route("/") # the argument is the URL endpoint
@app.route("/hello")
def say_hi(): # this function will be run at either endpoint (decorated by route)
    return "Hello world!"
    
@app.route("/hello/<name>")
def say_hi_again(name):
    return "Hello {}!".format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi = (last[0:3] + first[0:2]).title();
    print(jedi)
    return_string = """
    Your original name was {0} {1}\n
    Your jedi name is {2}""".format(first.title(), last.title(), jedi)
    return return_string;
    
#when you don't specify what type of data you return, Flask assumes that you are sending HTML

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))