import smtplib
from email.mime.text import MIMEText
_user = "1196234610@qq.com"
_pwd  = "afsabjrrqqdsgfgj"
_to   = "ctios@outlook.com"

msg = MIMEText("每日情话")
msg["Subject"] = ""
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print("Success!")
except smtplib.SMTPException:
    print("Falied")