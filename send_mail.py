import smtplib,sys
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
sender = 'your_sender@qq.com'
password = ''

def send_mail(receiver,sub,content):
	msg = MIMEText(content,_subtype='html',_charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = sender
	msg['To'] = ";".join(receiver)
	try:
		s =smtplib.SMTP()
		s.connect(mail_host)
		s.login(sender,password)
		s.sendmail(sender,receiver,msg.as_string())
		s.close()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	send_mail('you_send_to@qq.com','title','test')