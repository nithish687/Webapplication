from flask import Flask,render_template
from database import engine
from sqlalchemy import text
application  = Flask(__name__)

def user_names_db():
 with engine.connect() as conn:
  result = conn.execute(text("select * from details"))
  user_names = []
  for name in result.all():
    user_names.append(dict(name))
  return user_names

@application.route("/")

def app():
  user_name = user_names_db()
  return render_template('homepage.html',user_name = user_name)
  
if __name__ == "__main__":
  application.run(host='0.0.0.0',debug=True)

