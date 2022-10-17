import smtplib
from email.message import EmailMessage


def email_alert(subject, body):
    user = "udaykiran2804@gmail.com"
    password = "isfvhstjxsafctii"
    receiver_email = "497_bt19@iiitkalyani.ac.in"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = receiver_email
    msg['from'] = user

    print(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


#email_alert('Shopping list', 'Shopping list contains of: 1. eggs 2. Milk')