class Script:
    def __init__(self):
        self.link="link"

    def setFinalTag(self):
        self.finalTag="<script src=\""+self.link+"\""+">"+"</script>\n"

    def createLink(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag

    def setLink(self,link):
        self.link=link
