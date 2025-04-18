import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage


from_email_addr = "20114335@mail.wit.ie"          
from_email_pass = "1bmynktgflzwjbade"                         
to_email_addr = "20114335@mail.wit.ie"                


def send_email(subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr

        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_pass)
        server.send_message(msg)
        server.quit()

        print("sented:", subject)
    except Exception as e:
        print("failed, e)


channel = 4 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

-
def callback(channel):
    if GPIO.input(channel): 
        print("dry")
        send_email("water plz")
    else: 
        print("wet")
   
    )


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


print("run")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("stopped")
finally:
    GPIO.cleanup()
