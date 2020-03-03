
import xlrd 

from create_certificate import createpage
#from create_certificate1 import createpage1
from send1 import mail
#from qr import qrfun


loc = ("hum.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 



for i in range (1,3):
    
    #name=sheet.cell_value(i,2)
    
    
    namei=sheet.cell_value(i,0)
    
    name=namei.upper()
    namec=namei.title()
    code=sheet.cell_value(i,11)
     #idno is a unique id which will be showed when the qr code is scanned
    #rmail=sheet.cell_value(i,2) #rmail is the receiver's mail
    body= "Hi "+namec+"\n"+'''Greetings from Team Dhishna
We are more than happy to have you here for our workshop.Hope we played a vital role in improving your skills.
Attaching with this mail is your certificate which can be used in your CV or added to your Linkedin profile as a proof of your skill acquisition.
Wishing you all the very best and hoping to you soon on Dhishna.

Regards,
Dhishna 2020
    '''
    body1="Hi "+namec+"\n"+'''Greetings from Team Dhishna
Thank you for attending the Humanoid Workshop.Here is the verification code for the Utkranti Certificate.'''+code+"\n"+'''Regards,
Dhishna 2020'''
    
    print(name)
    print(namei)
    print(namec)
    print(body1)
    #image = qrfun(idno)         #calling function to generate qr code. Return the QR code image 
    rmail="megharose15@gmail.com"
    #createpage(name)   #calling function to create pdf
    #createpage1(name)
    print(rmail)
    #print("certificates gen "+name)
    #mail(rmail,body)        
    #mail("jyothisp52@gmail.com",body)    
    print("before")            
    mail(rmail,body1)   #calling function to send mail
    print("mail send to "+name)
    #mail(rmail,body)
    
    

