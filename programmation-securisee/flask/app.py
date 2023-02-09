from flask import Flask #import library
app = Flask(__name__) #instantiate new application

@app.route('/') #this is a decorator (attach the following function to 'app.route')
def index():
    return render_template("index.html")
