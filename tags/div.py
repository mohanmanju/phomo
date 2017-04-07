class Div:
    def __init__(self):
        self.width=""
        self.height=""

        self.items=[]
        self.finalTag="<div>\n</div>"

    def createDiv(self):
        self.setFinalTag()
        return self.finalTag

    def setFinalTag(self):
        self.finalTag="<div"+" height=\""+self.height+"\" width=\""+self.width+"\" >\n</div>"
        idx=self.finalTag.rfind("</div>")
        self.finalTag=self.finalTag[:idx]

        itemList=""
        for i in range(len(self.items)):
            itemList+=str(self.items[i])+"\n"

        self.finalTag+=itemList+"</div>"
        #self.finalTag=""



    def add(self,item):
        self.items.append(item)

    def __str__(self):
        return self.finalTag

    def setHeight(self,height):
        self.height=height

    def setWidth(self,width):
        self.width=width
