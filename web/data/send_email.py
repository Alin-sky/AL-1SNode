from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
import os
from flask import Flask

app = Flask(__name__, template_folder=os.path.dirname(os.path.realpath(__file__)))
current_directory = os.getcwd()
print(current_directory)

@app.route('/send_email', methods=['POST'])
def send_email():
    message = request.form.get('message')
    option = request.form.get('option', default="")  # Get the value of the option input
    send_email_to_qq(option, message)
    return render_template("return.html")

def send_email_to_qq(option, message):
    smtp_server = 'smtp.qq.com'
    sender = 'lvdonglin514@qq.com'
    password = 'hrqgtkhekdaniahh'  # Use the SMTP authorization code, not your QQ account password.
    receiver = 'lvdonglin514@qq.com'
    combined_message = f"Option: {option}\nMessage: {message}" 

    msg = MIMEText(combined_message, 'plain', 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = '网页信息'

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
    app.run(host='0.0.0.0')