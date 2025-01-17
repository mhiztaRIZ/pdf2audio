import webbrowser

import customtkinter
from customtkinter import *
from PIL import Image

from PyPDF4.pdf import PdfFileReader
import pyttsx3

# Declaring global variables related to PDF to Speech conversion
start_pgNo = None
end_pgNo = None


# Function to open the PDF selected and read text from it
def read():
    global start_pgNo, end_pgNo

    path = filedialog.askopenfilename()
    pdfLoc = open(path, 'rb')
    pdfreader = PdfFileReader(pdfLoc)
    speaker = pyttsx3.init()

    start = start_pgNo.get()
    end = end_pgNo.get()

    for i in range(start, end + 1):
        page = pdfreader.getPage(i)
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()

# contact function
def contact():
    url ='https://wa.link/5rjgsj'
    webbrowser.open(url)


# Function to create a GUI and get required inputs for PDF to Audio Conversion
def pdf_to_audio():
    global start_pgNo, end_pgNo

    wn1 = customtkinter.CTk()
    wn1.title("PDF to Audio converter")
    wn1.geometry('690x400')
    wn1.config(bg = 'skyblue')

    start_pgNo = IntVar(wn1)
    end_pgNo = IntVar(wn1)

    CTkLabel(wn1, text = 'PDF to Audio converter', fg_color = 'skyblue', text_color = 'black', font =('Comic Sans MS',
                                                                                                      20)).grid(padx=60,
                                                                                                                pady=20)

    CTkLabel(wn1, text = 'Enter the start and the end page to read. To read a single page,\n'
                         'enter the start page and enter the next page as the end page:',
             anchor = "sw", justify = LEFT, fg_color = 'skyblue', text_color = 'black', font =('Comic Sans MS',
                                                                                               16)).grid(padx = 20,
                                                                                                         pady = 10)

    CTkLabel(wn1, text = 'Start Page No:', fg_color = 'skyblue', text_color = 'black', font =('Comic Sans MS',
                                                                                              16)).grid(row = 3,
                                                                                                        column = 0,
                                                                                                        padx = 100,
                                                                                                        pady = 20,
                                                                                                        sticky = 'w')
    startPg = CTkEntry(wn1, width = 30, textvariable = start_pgNo)
    startPg.grid(row = 4, column = 0, padx = 132, pady = 10, sticky = 'w')

    CTkLabel(wn1, text = 'End Page No:', fg_color = 'skyblue', text_color = 'black', font =('Comic Sans MS',
                                                                                            16)).grid(row = 3,
                                                                                                      column = 0,
                                                                                                      padx = 100,
                                                                                                      pady = 20,
                                                                                                      sticky = 'e')
    endPg = CTkEntry(wn1, width = 30, textvariable = end_pgNo)
    endPg.grid(row = 4, column = 0, padx = 132, pady = 10, sticky = 'e')

    CTkLabel(wn1, text = 'Click the below button to Choose the pdf file, select the file to start playback:',
             fg_color = 'skyblue',
             text_color = 'black',
             font =('Comic Sans MS',16)).grid(padx = 100, pady = 10)

    CTkButton(wn1, text = "Click Me", bg_color = 'ivory3', font = ('Comic Sans MS', 17),
              command = read).grid(row = 6, column = 0, padx = 150, pady = 10, sticky = 'w')

    CTkButton(wn1, text = 'Contact Us', bg_color = 'ivory3', font = ('Comic Sans MS', 17),
              command = contact).grid(row = 6, column = 0, padx = 150, pady = 10, sticky = 'e')

    wn1.mainloop()


# Declaring global variable for PDF to Speech conversion
global pdfPath


# Creating the main window
wn = customtkinter.CTk()
wn.title("PDF to Audio converter... built by Riz")
wn.geometry('700x300')
wn.config(bg = 'skyblue')
image = customtkinter.CTkImage(Image.open('monnify.png'), size = (100, 100))

CTkLabel(wn, image = image, text = 'PDF to Audio converter', fg_color = 'skyblue', text_color = 'black',
         font =('Comic Sans MS', 20)).grid(padx = 40,
                                           pady = 20)

CTkButton(wn, text = "Convert PDF to Audio", bg_color = 'ivory3', font =('Comic Sans MS', 17),
          command = pdf_to_audio).grid(padx = 230, pady = 20)

CTkLabel(wn, text = 'Built with ❤ by Riz using PY', fg_color = 'skyblue', text_color = 'black',
         font = ('Comic Sans MS', 16)).grid(padx = 230, pady = 10)


# Runs the window till it is closed
wn.mainloop()
