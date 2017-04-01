class Title:
    def __init__(self):
        self.text=""
    def setFinalTag(self):
        self.finalTag="<title>"+self.text+"</title>"

    def createTitle(self):
        self.setFinalTag()
        return self.finalTag

    def setText(self,text):
        self.text=text
