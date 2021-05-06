#YES OR NO .
from random import randint
answer=["Yes","No"]
for i in range(3):
   print(answer[randint(0,1)])




#daytime:
from datetime import datetime
now = datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))




#number guesser 
#a game to guess a number from 0 to x
import random
def number_guesser(x):
      numero_choisi=random.randint(0,x)
      while True:
          num=int(input("veuillez saisir le numéro "))
          if num > numero_choisi:
             print("a little less")
          elif num < numero_choisi:
              print("a little more")
          else:
              return ("You found the number !!!")
            #"return" ends the function ( same effect if we use print then break)




#random password generator
def pass_generator():
    import random,string
    liste_de_car =(string.ascii_lowercase+string.ascii_uppercase+"~#{[|`\^@]}&é(-è_çà)=+-*/,;:!?§")
    len_pass= int(input("veuillez saisir la longuer de votre mot de passe  :  "))
    mdp=""
    for i in range(len_pass):
        mdp+=liste_de_car[random.randint(0,len(liste_de_car)-1)]
    return mdp




#calcul moyenne
def calc(nb_matiere):
    somme_notes=0
    somme_coefficients=0
    for i in range(nb_matiere):
        note = float(input("veuillez saisir la note de la matière                "))
        coeff= float(input("veuillez saisir le coefficient de cette matiere  "))
        somme_notes+=note*coeff
        somme_coefficients+=coeff
    return somme_notes/somme_coefficients     




#turning pdf to audio book
import pyttsx3, PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('WRITE THE PDF FILE PATH','rb'))
#write the pdf's file path above inside "open" and before "rb"
speaker = pyttsx3.init()
for page_num in range(8,pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()




#Youtube vid down 
 #simple
from pytube import YouTube
url=YouTube("https://www.youtube.com/watch?v=-dj6jJrAMW8&list=RDMM-dj6jJrAMW8&start_radio=1")
#you can change paste your preferred video link above for the video that you want to downlaod
video = url.streams.first()
video.download()




 #with ui
from tkinter import *
#standard GUI(graphical user interface library).
from pytube import YouTube
#used to download videos from youtube
win = Tk()
#setting the name for the win
win.geometry("1300x1050")
#set a fixed size for the win
win.title("Youtube Video Downloader")
#gives a title de the win
Label(win,text = 'Youtube Video Downloader', font =('Times New Roman',20)).pack()
#.pack() puts automatically what is needed to be put ,for example we can use .place(x=550,y=150) instead with you controlling the specific placement with x and y coordenates
#font is optional, it serves to set the font and font size for the text
#displays a text
link = StringVar()
#stores the video link
Label(win, text = 'Paste Link Here:', font = ('Times New Roman',15)).pack()
link_enter = Entry(win, width = 70,textvariable = link).pack()
#entry is used to create an input text field
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(win, text = 'DOWNLOADED', font = ('Times New Roman',15),bg='green').pack()  
Button(win,text = 'DOWNLOAD', font = ('Times New Roman',15) ,bg = 'red',  command = Downloader).pack()
win.mainloop()
#a method to excute the program

 
