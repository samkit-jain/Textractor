import urllib.request

from html.parser import HTMLParser


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global isp, ish, isa

        if str(tag) == "p":
            isp = True
        elif str(tag) == "h1" or str(tag) == "h2" or str(tag) == "h3" or str(tag) == "h4" or str(tag) == "h5" or str(tag) == "h6":
            ish = True
        elif str(tag) == "a":
            isa = True

    def handle_endtag(self, tag):
        global isp, ish, isa

        if str(tag) == "p":
            isp = False
            print()
            print()
        elif str(tag) == "h1" or str(tag) == "h2" or str(tag) == "h3" or str(tag) == "h4" or str(tag) == "h5" or str(tag) == "h6":
            ish = False
            print()
            print()
        elif str(tag) == "a":
            if isp == False and ish == False:
                print()
                print()
            isa = False

    def handle_data(self, data):
        global isp, ish, isa

        if not data.isspace():
            if isp == True or ish == True:
                print(data, end="")
            elif isp == False and ish == False and isa == True:
                print(data, end="")


isp = False
ish = False
isa = False
link = "http://computemagazine.com/man-who-invented-world-wide-web-gives-new-definition/" #url goes here

req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
op = urllib.request.urlopen(req)
source_code = op.read()

parser = Parser()
parser.feed(str(source_code.decode("utf-8")).replace('\n', ' '))
