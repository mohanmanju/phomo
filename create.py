import webbrowser
from tags.input import *
from tags.html import *
from tags.div import *
from tags.para import *
from tags.form import *

Html.startHtml()
Html.startBody()
f=Div()
i=Input()
i.setType("username")
p=Input()
p.setType("password")

#i.createInput()
#p.createInput()


f.setHeight("345")
f.setWidth("567")
f.write("jhvsd")
f.add(i)
f.write("jhdbfj")
f.add(p)
f.createDiv()
Html.endBody()
Html.endHtml()
