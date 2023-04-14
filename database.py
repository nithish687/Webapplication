from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://2udg12wufjre0c4ycdlh:pscale_pw_JAtZn9AjDIknTMO6fASUG0aRdiAmk3bQvBRxRy8WqvD@aws.connect.psdb.cloud/nitish?charset=utf8mb4",connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

with engine.connect() as conn:
  result = conn.execute(text("select * from details"))
  print(result.all())