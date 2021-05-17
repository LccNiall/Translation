import speech_recognition as sr
import tkinter as tk
import threading
from tkinter import *
class App:

    def __init__ (self,master):
        self.mainGui(master)




    def recognizeMic(self):
        r = sr.Recognizer()

        self.mic = sr.Microphone()
        with self.mic as source:
            try:
                print("begun listening")

                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                self.audioResult = r.recognize_google(audio)

                self.listenResult['text'] = self.listenResult['text'] + ' ' + self.audioResult
                print(r.recognize_google(audio))
                print("stopped listening")

            except:
                print("No audio detected, speak louder")


    def mainGui(self,master):


        self.mainFrame = Frame(master, padx=100, pady=50, bg="#abbcbc", bd=6, relief="solid")
        self.mainFrame.pack(fill=BOTH, expand=True)

        self.listenResult = Label(self.mainFrame,width=1000,height=10, text="")
        self.listenResult.pack()

        self.listenButton = Button(self.mainFrame,text="Begin Listening",command=lambda: self.getListen())
        self.listenButton.pack()

        self.listenButton.bind('<ButtonPress-1>', self.keepListen())
        self.listenButton.bind('<ButtonRelease-1>', self.stoplisten())

        self.stopButton = Button(self.mainFrame, text="Stop Listening", command=lambda: self.stoplisten())
        self.stopButton.pack()

    def getListen(self):
        x = threading.Thread(target=self.recognizeMic, args=())

        #self.isListening = True

        x.start()


    def keepListen(self):

        self.timeListening = 5

    def stoplisten(self):
        self.isListening = False
        self.timeListening = 1

def createWindow():

    global textResult
    textResult = ""

    global root

    root = Tk()

    root.title("Speech recognition")

    root.geometry('550x550')

    app = App(root)

    root.mainloop()


createWindow()
