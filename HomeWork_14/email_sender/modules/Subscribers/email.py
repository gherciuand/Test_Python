import smtplib
from socket import gaierror



def sendemail(addressTo, name, adressFrom):
    print(f'Sending email to {addressTo} from {adressFrom}....')

    port = 587
    smtp_server = "smtp.gmail.com"
    login = adressFrom
    password = "*****_*****"

    message = f"Hi {name}, \n\n" \
              f"I send this message using Python"

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(adressFrom, addressTo, message)

        print(f'Message sent to {name}')
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
