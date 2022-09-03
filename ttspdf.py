import PyPDF2
import pyttsx3

class Reading:

    path=open(r'C:\Users\ABEL\Desktop\MODULE3- SS&C.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(path)
    from_page = pdfReader.getPage(21)
    text = from_page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()