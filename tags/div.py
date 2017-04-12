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
        self.finalTag="<div"+" height=\""+self.height+"px\" width=\""+self.width+"px\" >\n</div>"
        idx=self.finalTag.rfind("</div>")
        self.finalTag=self.finalTag[:idx]

        itemList=""
        for i in range(len(self.items)):
            itemList+=str(self.items[i])+"\n"

        self.finalTag+=itemList+"</div>"

        fo=open("1.html","a")
        fo.write(self.finalTag+"\n")
        #self.finalTag=""



    def add(self,item):
        self.items.append(item)

    def __str__(self):
        return self.finalTag

    def setHeight(self,height):
        self.height=height

    def setWidth(self,width):
        self.width=width

    def write(self,text):
        self.items.append(text)
