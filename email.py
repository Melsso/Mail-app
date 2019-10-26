import smtplib
# open a file with the list of emails.
with open("out","r") as f:
    l = f.read()

l = l.split("\n")
l = [i for i in l if "@" in i]

# open the file that has the message you want to send.

with open("file.txt","r") as f:
	msg = f.read()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()

s.login("TYPE YOUR EMAIL HERE","TYPE YOUR PASSWORD HERE")

for i in l:
	print (i)
	s.sendmail("TYPE YOUR EMAIL HERE",i,"Subject: TYPE THE SUBJECT HERE\n\n" + msg)
		
print("Done")