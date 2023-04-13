from flask import Flask,render_template


application  = Flask(__name__)

@application.route("/")
def app():
  return render_template('homepage.html')
if __name__ == "__main__":
  application.run(host='0.0.0.0',debug=True)