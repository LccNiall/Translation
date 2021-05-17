import speech_recognition as sr
import tkinter as tk
import threading
from tkinter import *
from translate import Translator
import time


class App:

    def __init__ (self,master):
        self.mainGui(master)
        self.isRunningRecognizer = False


    def recognizeMic(self,lang,which):
        r = sr.Recognizer()

        self.mic = sr.Microphone()

        n = 0
        if(which == 1):
            self.translator = Translator(to_lang=lang)
        elif(which == 2):
            self.translator = Translator(from_lang=lang,to_lang="en")
        #while (self.isRunningRecognizer and n == 0):
        with self.mic as source:
            try:
                    while self.isRunningRecognizer:
                        self.isRecordingLabel['text'] = "Recording"
                        self.isRecordingLabel.pack()


                        r.adjust_for_ambient_noise(source, duration=0.5)
                        #time.sleep(0.5)
                        print("Begun listening")


                        audio = r.record(source,duration=5)

                        self.audioResult = r.recognize_google(audio)
                        #self.audioResult = r.recognize_google(audio)
                        if(which == 1):
                            self.audioResult = r.recognize_google(audio)
                        elif(which == 2):
                            self.audioResult = r.recognize_google(audio, language = "es-AR")

                        self.isRecordingLabel['text'] = "Recording.."

                        translation = self.translator.translate(self.audioResult)
                        if(which == 1):
                            self.listenResult['text'] = self.listenResult['text'] + ' ' + translation
                        elif(which == 2):
                            self.listenResult2['text'] = self.listenResult2['text'] + ' ' + translation

                        #print(r.recognize_google(audio))
                    self.isRecordingLabel['text'] = ""
                    print("Stopped listening")
                    #n += 1
            except:
                    print("No audio detected, speak louder")
                    #n += 1

        print("exited")

    def mainGui(self,master):


        self.mainFrame = Frame(master, padx=100, pady=50, bg="#abbcbc", bd=6, relief="solid")
        self.mainFrame.pack(fill=BOTH, expand=True)

        self.langBox = Entry(self.mainFrame)
        self.langBox.pack()

        self.listenResult = Label(self.mainFrame,width=1000,height=10, text="")
        self.listenResult.pack()

        self.listenButton = Button(self.mainFrame,text="Begin Listening",command=lambda: self.getListen(self.langBox.get(),1))
        self.listenButton.pack()

        #self.listenButton.bind('<ButtonPress-1>', self.keepListen())
        #self.listenButton.bind('<ButtonRelease-1>', self.stoplisten())

        self.stopButton = Button(self.mainFrame, text="Stop Listening", command=lambda: self.stoplisten())
        self.stopButton.pack()

        self.isRecordingLabel = Label(self.mainFrame,bg="#abbcbc")
        self.isRecordingLabel.pack()

        #self.langBox2 = Entry(self.mainFrame)
        #self.langBox2.pack()

        self.listenResult2 = Label(self.mainFrame, width=1000, height=10, text="")
        self.listenResult2.pack()

        self.listenButton2 = Button(self.mainFrame, text="Begin Listening", command=lambda: self.getListen(self.langBox.get(),2))
        self.listenButton2.pack()

        # self.listenButton.bind('<ButtonPress-1>', self.keepListen())
        # self.listenButton.bind('<ButtonRelease-1>', self.stoplisten())

        self.stopButton2 = Button(self.mainFrame, text="Stop Listening", command=lambda: self.stoplisten())
        self.stopButton2.pack()

        self.isRecordingLabel2 = Label(self.mainFrame, bg="#abbcbc")
        self.isRecordingLabel2.pack()


    def getListen(self,lang,which):
        self.isRunningRecognizer = True
        self.timeListening = 5.5
        self.x = threading.Thread(target=self.recognizeMic, args=(lang,which),daemon=True)

        #self.isListening = True

        self.x.start()



    def keepListen(self):

        self.timeListening = 1
        print("Keep listening")

    def stoplisten(self):
        self.isRunningRecognizer = False
        self.timeListening = 1
        print("StoppingListen")
        #self.x.join()


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
