# code adapted from: http://pythonstudy.xyz/python/article/508-%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0-SMTP

import smtplib
from email.mime.text import MIMEText
try:
    from .config import from_address, to_address, password
except:
    from_address = ''  # 미세먼지 알림을 보낼 메일 계정
    password = ''  # 위 계정의 패스워드
    to_address = ''  # 미세먼지 알림을 받을 메일 계정


def send_mail(content, smtp_server='smtp.gmail.com:587'):
    msg = MIMEText(content)
    msg['Subject'] = '미세먼지 주의!!!!'

    gmail_smtp_server = smtp_server
    smtp = smtplib.SMTP(gmail_smtp_server)
    smtp.starttls()
    smtp.login(from_address, password)
    smtp.sendmail(from_address, to_address, msg.as_string())
    smtp.quit()
