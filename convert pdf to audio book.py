# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:15:41 2022

@author: tt
"""

from gtts import gTTS
import os
language = 'en'

##Change it into an application format.
#Ask for a text string or a file directory.

def string_conversion():
    string_input = input("OK! Type a string you want to convert below:\n")
    output_file = gTTS(text=string_input, lang=language, slow=False)
    output_file.save("text_to_speach.mp3")
    os.system("start text_to_speach.mp3")

def pdf_conversion():
    file_endpoint_input = input("OK! Enter the full path of the file that you want to convert into a speach:\n")
    with open((file_endpoint_input)) as f:
        file_text =  f.read()
        
    
    output_file = gTTS(text=file_text, lang=language, slow=False)
    output_file.save("text_to_speach.mp3")
    os.system("start text_to_speach.mp3")


type_input = input("What would you like to convert into speach-form, a string or a pdf/doc file?\n Type 's' or 'string' for string and 'p' or 'pdf for a pdf file or 'd' or 'doc' or 'docx' for a docx file.\n")

if type_input.lower() == "s" or type_input.lower() == "string":
    string_conversion()
elif type_input.lower() == "p" or type_input.lower() == "pdf" or type_input.lower() == "doc" or type_input.lower() == "docx" or type_input.lower() == "d":
    pdf_conversion()
else:
    print("Something went wrong.\n Try again later")