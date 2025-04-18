import smtplib
from email.message import EmailMessage


from_email_addr = "20114335@mail.wit.ie"


from_email_pass = "114514"


to_email_addr = "1606464637@qq.com"


msg = EmailMessage()
msg.set_content("hello RPI")
msg['Subject'] = "Test text"
msg['From'] = from_email_addr
msg['To'] = to_email_addr



server = smtplib.SMTP('smtp.office365.com', 587)  
server.starttls()  
server.login(from_email_addr, from_email_passserver.send_message(msg) )
print("")

server.quit()
