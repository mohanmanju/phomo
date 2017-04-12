class Para:
    def __init__(self):
        self.text=""
    def setFinalTag(self):
        self.finalTag="<p>"+self.text+"</p>\n"

    def createPara(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag

    def setText(self,text):
        self.text=text

    def __str__(self):
        return self.createPara()
