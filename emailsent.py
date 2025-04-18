import smtplib
from email.message import EmailMessage


from_email_addr = "1606464637@qq.com"


from_email_pass = "bmynktgflzwjbade"


to_email_addr = "3188213735@qq.com"


msg = EmailMessage()
msg.set_content("hello RPI")
msg['Subject'] = "Test text"
msg['From'] = from_email_addr
msg['To'] = to_email_addr



server = smtplib.SMTP('smtp.qq.com',587)  
server.starttls()  
server.login(from_email_addr, from_email_pass)
server.send_message(msg)
print("Email sent")

server.quit()
