import webbrowser

class Html:

    def startHtml():
        print("main")
        fo=open("1.html","w")
        fo.write("<html>\n<head>\n")

    def startBody():
        fo=open("1.html","a")
        fo.write("</head>\n<body>\n")

    def endBody():
        fo=open("1.html","a")
        fo.write("</body>\n")

    def endHtml():
        fo=open("1.html","a")
        fo.write("</html>\n")
        url = "/home/raghu/Music/phomo/1.html"
        webbrowser.open(url,new="")

    def write(text):
        fo=open("1.html","a")
        fo.write(text)

    def insertTag(text):
        fo=open("1.html","a")
        fo.write(text,"\n")
