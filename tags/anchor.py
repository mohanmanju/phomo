class Anchor:
    def __init__(self):
        self.link="link"
        self.name="name"


    def setFinalTag(self):
        self.finalTag="<a href=\""+self.link+"\""+">"+self.name+"</a>\n"

    def createAnchor(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag

    def setName(self,name):
        self.name=name

    def setLink(self,link):
        self.link=link

    def __str__(self):
        return self.createAnchor()
