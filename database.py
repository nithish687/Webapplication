from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://4tgzmpc9q977lyyedh0m:pscale_pw_tcXTpnJVA4Rp6aE5T7JnMH1PzlZoz3mN9boy2fhvc3W@aws.connect.psdb.cloud/nitish?charset=utf8mb4",
connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


with engine.connect() as conn:
  result = conn.execute(text("select * from details"))
  return result.all()

