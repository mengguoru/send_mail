import smtplib
from email.header import Header 
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
sender = 'your_sender@163.com'
password = '***'

def send_mail(receiver,sub,content):
	s = smtplib.SMTP(mail_host,25)
	s.login(sender,password)

	msg = MIMEText(content,'plain','utf-8')
	msg['From'] = sender
	msg['To'] = receiver
	msg['Subject'] = Header(str(sub))
	try:
		s.sendmail(sender,[receiver],msg.as_string())
	except Exception as e:
		raise e
	finally:
		s.close()
	

if __name__ == '__main__':
	send_mail('you_send_to@qq.com','title','test')