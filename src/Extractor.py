import urllib.request
import os

from html.parser import HTMLParser


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global isp, ish, isa, isul, isol, countli

        if str(tag) == "p":
            isp = True
        elif str(tag) == "h1" or str(tag) == "h2" or str(tag) == "h3" or str(tag) == "h4" or str(tag) == "h5" or str(
                tag) == "h6":
            ish = True
        elif str(tag) == "a":
            isa = True
        elif str(tag) == "ul":
            isul = True
            countli = 0
        elif str(tag) == "ol":
            isol = True
            countli = 0
        elif str(tag) == "li":
            countli += 1

    def handle_endtag(self, tag):
        global isp, ish, isa, isul, isol, countli

        if str(tag) == "p":
            isp = False
            print()
            print()
        elif str(tag) == "h1" or str(tag) == "h2" or str(tag) == "h3" or str(tag) == "h4" or str(tag) == "h5" or str(
                tag) == "h6":
            ish = False
            print()
            print()
        elif str(tag) == "a":
            if isp == False and ish == False:
                print()
                print()
            isa = False
        elif str(tag) == "ul":
            isul = False
            print()
        elif str(tag) == "ol":
            isol = False
            print()

    def handle_data(self, data):
        global isp, ish, isa, isul, isol, countli

        if not data.isspace():
            if isp == True or ish == True:
                print(data, end="")
            elif isp == False and ish == False and isa == True:
                print(data, end="")
            elif isul == True or isol == True:
                print(countli, " ", data)


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

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        op = urllib.request.urlopen(req, timeout=1)
        source_code = op.read()

        parser = Parser()
        parser.feed(str(source_code.decode("utf-8")).replace('\n', ' '))
    except urllib.error.URLError:
        show_error()


def default():
    url = "http://computemagazine.com/man-who-invented-world-wide-web-gives-new-definition/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        op = urllib.request.urlopen(req, timeout=1)
        source_code = op.read()

        parser = Parser()
        parser.feed(str(source_code.decode("utf-8")).replace('\n', ' '))
    except urllib.error.URLError:
        show_error()


def from_file(location):
    clear_screen()

    if location[-5:] != '.html':
        print("Extension of the file should be .html   -_-")
    else:
        file = open(location, 'r')
        source_code = file.read()
        parser = Parser()
        parser.feed(source_code.replace('\n', ' '))


isp = False
ish = False
isa = False
isol = False
isul = False
countli = 0

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
