from  get_content import get_content
from send_mail import  send_mail

if __name__ == '__main__':
	data = get_content()
	send_mail('you_send_to@qq.com','title',data)