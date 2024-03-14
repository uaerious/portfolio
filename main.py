from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
  if request.method == "POST":
    name = request.form['name']
    email = request.form['email']
    file = open("test.txt", 'a')
    file.write(name + email + '\n') # does it work? idk didnt try
    file.close()
    return render_template('index.html',name=name,email=email)
  return render_template('index.html') # for get method


app.run(host='0.0.0.0', port=81)
