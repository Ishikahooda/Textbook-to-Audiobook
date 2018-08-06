import sys
from gtts import gTTS
from os import chdir, getcwd, listdir, path
import PyPDF2

def check_path(prompt):

    ''' (str) -> str
    Verifies if the provided absolute path does exist.
    '''

    abs_path = input(prompt)
    while path.exists(abs_path) != True:
        print("\nThe specified path does not exist.\n")
        abs_path = input(prompt)
    return abs_path

print("\n")
pdf_name = check_path("Provide absolute path for the folder: ")
#pdf_name = 'TwinkleTwinkle.pdf'
pdfObj = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    print(text)
speech = gTTS(text)
speech.save("audio.mp3")

pdfObj.close()
