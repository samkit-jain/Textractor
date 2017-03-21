import pdfkit
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def show_menu():
    print("I want to ")
    print("1. input URL of the webpage")
    print("2. input location (local) of an HTML file")
    print("3. use default URL - http://computemagazine.com/man-who-invented-world-wide-web-gives-new-definition/\n")


def show_error():
    print("You may not have a working internet connection :(")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def user_input(url):
    clear_screen()

    pdfkit.from_url(url, 'output.pdf')

    print convert_pdf_to_txt('output.pdf')


def default():
    url = "http://computemagazine.com/man-who-invented-world-wide-web-gives-new-definition/"
    
    user_input(url)


def from_file(location):
    clear_screen()

    if location[-5:] != '.html':
        print("Extension of the file should be .html   -_-")
    else:
        pdfkit.from_file(location, 'output.pdf')
        
        print convert_pdf_to_txt('output.pdf')


clear_screen()
show_menu()
choice = int(input("Enter choice (1, 2, 3) - "))

while choice not in {1, 2, 3}:
    clear_screen()
    print("Option not available! Please try again :)\n")
    show_menu()
    choice = int(input("Enter choice (1, 2, 3) - "))

clear_screen()

if choice == 1:
    link = input("Input URL - ")
    user_input(link)
elif choice == 2:
    loc = input("Input file location - ")
    from_file(loc)
elif choice == 3:
    default()
