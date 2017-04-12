class Button:
    def __init__(self):
        self.onclick=""
        self.value="value"
        self.finalTag=""

    #changing final tag to changed values
    def setFinalTag(self):
        #final string to represent a tag in html
        self.finalTag="<button onclick=\""+self.onclick+"\" > "+ self.value+ " </button>\n"

    #creating input using this methods
    def createButton(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag


    #set value to input field
    def setValue(self,value):
        self.value=value

    def setOnclick(self,value):
        self.onclick=value

    #get string eqivalent of the tags
    def __str__(self):
        return self.createInput()
