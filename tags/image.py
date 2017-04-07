class Image:
    def __init__(self):
        self.source="source"
        self.alt="alt"
        self.height="height"
        self.width="width"


    def setFinalTag(self):
        self.finalTag="<img src=\""+self.source+"\" "+"alt=\""+self.alt+"\" "+"height=\" "+self.height+"\" width=\""+self.width+"\">"

    def createImage(self):
        self.setFinalTag()
        return self.finalTag

    def setSource(self,source):
        self.source=source

    def setAlt(self,alt):
        self.alt=alt

    def setHeight(self,height):
        self.height=height

    def setWidth(self,width):
        self.width=width
