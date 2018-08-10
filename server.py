from flask import Flask, jsonify, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail_settings = {
  "MAIL_SERVER": "smtp.gmail.com",
  "MAIL_PORT": 465,
  "MAIL_USE_TLS": False,
  "MAIL_USE_SSL": True,
  "MAIL_USERNAME": os.environ['MY_EMAIL'],
  "MAIL_PASSWORD": os.environ['MY_PASSWORD']
}
app.config.update(mail_settings)
mail = Mail(app)

@app.route('/email', methods=['POST'])
def send_email():
    req = request.get_json()
    body_msg = req['message']
    sender_email = req['email_address']
    msg = Message(subject="Test",
                  sender='{}'.format(sender_email),
                  recipients=["{}".format(app.config.get('MAIL_USERNAME'))],
                  body='{}'.format(body_msg))
    mail.send(msg)
    return 'Sent'