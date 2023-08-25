from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    message = request.form['message']
    send_email_to_qq(message)
    return "Email sent successfully"

def send_email_to_qq(message):
    smtp_server = 'smtp.qq.com'
    sender = 'lvdonglin514@qq.com'
    password = 'hrqgtkhekdaniahh'
    receiver = 'lvdonglin514@qq.com'

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = '网页信息'

    server = smtplib.SMTP_SSL(smtp_server)
    server.login(sender, password)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
    try:
        server = smtplib.SMTP_SSL(smtp_server)
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        print("已成功提交,我们会及时处理")
    except smtplib.SMTPException as e:
        print("Error: unable to send email. Error message:", e)
@app.route('/')
def home():
    return "Hello, World!"
if __name__ == '__main__':
    app.run()
    

