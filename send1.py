import email, smtplib, ssl


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





subject = "Dhishna"
sender_email = "tech.dhishna@gmail.com"
password = "SantyDance"
# password = input("Type your password and press enter:")


def mail(receiver_email, body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "Dhishna <tech.dhishna@gmail.com>"
    # message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = sender_email  # Recommended for mass emails (sending one email to multiple recepients) Not our case.

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    #filename1 = "certificate1.pdf"

    

    # Encode file in ASCII characters to send by email    
    
    text = message.as_string()


    # Open PDF file in binary mode
    #with open(filename1, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        #part1 = MIMEBase("application", "octet-stream")
        #part1.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    #encoders.encode_base64(part1)

    # Add header as key/value pair to attachment part
    #part1.add_header(
         #"Content-Disposition",
         #f"attachment; filename= {filename1}",
     #)

    # Add attachment to message and convert message to string
    #message.attach(part1)
    #text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    print('y')

    print("hey")

if __name__ == "__main__":
    receiver_email = "megharose15@gmail.com"
    body = "This is an email with attachment sent from Python"
    mail(receiver_email, body)
    print("sdf")


