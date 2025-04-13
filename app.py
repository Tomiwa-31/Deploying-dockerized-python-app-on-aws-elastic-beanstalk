from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "hello tomiwa - this is our demo on elasticbeanstalk"

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=3000)