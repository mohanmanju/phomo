class Link:
    def __init__(self):
        self.link="link"
        #self.rel="rel"
        self.type="type"

    def setFinalTag(self):
        self.finalTag="<link rel=\"stylesheet\" "+"type=\""+self.type+"\" "+"href=\""+self.link+"\""+">\n"

    def createLink(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag

    #def setRel(self,name):
        #self.rel=name

    def setType(self,name):
        self.type=name

    def setLink(self,link):
        self.link=link
