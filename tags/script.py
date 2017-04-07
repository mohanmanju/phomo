class Script:
    def __init__(self):
        self.link="link"

    def setFinalTag(self):
        self.finalTag="<script src=\""+self.link+"\""+">"+"</script>"

    def createLink(self):
        self.setFinalTag()
        return self.finalTag

    def setLink(self,link):
        self.link=link
