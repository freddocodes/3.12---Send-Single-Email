import yagmail
import os

sender = 'farid@dakotazl.com'
receiver = 'elneser.farid@gmail.com'

subject = "This is the Subject"


contents = "Here is the content of the email, HELLO !"

yag = yagmail.SMTP(user=sender, password=os.getenv('APPASS'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
