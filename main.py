import smtplib
import pyttsx3
import speech_recognition as sr
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # have to make sure to give access in our google account
    server.login('Sender Mail', 'Password')
    email = EmailMessage()
    email['From'] = 'Mail'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'mentor': 'jhanker.mahbub@gmail.com',
    'programming': 'support@python-programming@gmail.com',
    'lisa': 'lisa@blackpink.com',
    'osama': 'osama.bin@laden.com',
    'iphone': 'support@apple.com'
}


def get_email_info():
    talk('To whom you wanna send a mail')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What will be the subject line?')
    subject = get_info()
    talk('Tell me the text of your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Voila, Your email has been sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()