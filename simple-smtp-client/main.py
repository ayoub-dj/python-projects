from decouple import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = config('SMTPHOST', cast=str)
port = config('SMTPPORT', cast=int)
user = config('SMTPUSER', cast=str)
password = config('SMTPPASSWORD', cast=str)

subject = 'Test email from python script'
body_plain_text = 'You what\'s UP'
html_body = """
<html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h1 style="color: #333;">Hello!</h1>
            <p style="color: #555; line-height: 1.5;">This is a stylish HTML email sent to multiple recipients from Python!</p>
            <p style="color: #555; line-height: 1.5;">We hope you find this email informative and well-designed.</p>
            <p style="color: #555; line-height: 1.5;">Have a great day!</p>
            <div style="margin-top: 20px; font-size: 12px; color: #999;">This is an automated message. Please do not reply.</div>
        </div>
    </body>
</html>
"""
recipient_email = 'email@example.com'
recipient_emails = [
    'email@example.com',
    'email@example.com',
]


message = MIMEMultipart()
message['from'] = user
# message['to'] = recipient_email
message['to'] = ', '.join(recipient_emails)
message['subject'] = subject

message.attach(MIMEText(html_body, 'html'))

def sending():
    try:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, password)
            # server.sendmail(user, recipient_email, message.as_string())
            server.sendmail(user, recipient_emails, message.as_string())
            print('Email Sent')
    except Exception as e:
        print(f'Error {e}')

if __name__ == '__main__':
    sending()