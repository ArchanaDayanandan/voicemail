import speech_recognition as sr     # import the library
import smtplib 
#import mysql.connector


 #mydb = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #passwd="",
  #database="voicemail"
#)

r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))# creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("achu640@gmail.com", "ammukuttyachu123") 
        
        # message to be sent 
        message =text
        
        # sending the mail 
        s.sendmail("achu640@gmail.com", "archanadayanandan95@gmail.com", message) 
        
        # terminating the session 
        s.quit()
       # mycursor = mydb.cursor()
        

       # sql = "INSERT INTO outbox (content) VALUES ('"+text+"')"

       # mycursor.execute(sql)

       # mydb.commit()
    except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly