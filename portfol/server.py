from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
   return render_template('index.html')

@app.route("/index.html")
def hey():
   return render_template('index.html')

@app.route("/contact.html")
def blog():
    return render_template('contact.html')

@app.route("/works.html")
def blog_2():
    return render_template('works.html')

@app.route("/favicon.ico")
def blog_5():
    return render_template('icon.html')

@app.route("/<string:pagename>")       
def blog_4(pagename):
    return render_template(pagename)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return 'Form Submitted'
    else:
        return 'Something went wrong. Try again.'

def get_data():
    pass

get_data()
