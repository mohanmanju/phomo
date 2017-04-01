class Para:
    def __init__(self):
        self.text=""
    def setFinalTag(self):
        self.finalTag="<p>"+self.text+"</p>"

    def createPara(self):
        self.setFinalTag()
        return self.finalTag

    def setText(self,text):
        self.text=text

    def __str__(self):
        return self.finalTag
