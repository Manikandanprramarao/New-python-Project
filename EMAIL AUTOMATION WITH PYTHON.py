#EMAIL AUTOMATION WITH PYTHON

   #Please Setup less secure app in gmail account

import smtplib    #Simple Mail Transfer Protocol

obj=smtplib.SMTP("smtp.gmail.com",587)
   #Transport layer Security
obj.starttls()  
   #login
mail_id = input("Enter your Gmail id : ")
password = input("Enter your Password : ")

obj.login(mail_id,password)

sub=input('enter a sub : ')
body=input('enter a messege : ')
messege="Subject:{}\n\n{}".format(sub,body)

obj.sendmail(mail_id,[input("Enter a Gmail id to sent : ")],messege)
print("mail sent successfully!!!!!!!!!")
