class Anchor:
    def __init__(self):
        self.link="link"
        self.name="name"


    def setFinalTag(self):
        self.finalTag="<a href=\""+self.link+"\""+">"+self.name+"</a>"

    def createAnchor(self):
        self.setFinalTag()
        return self.finalTag

    def setName(self,name):
        self.name=name

    def setLink(self,link):
        self.link=link
