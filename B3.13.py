class HTML:
    def __init__(self, html_or_print):
        self.html_or_print = html_or_print
        if self.html_or_print == "file":
            with  open("test.html", "w", encoding="utf-8") as writer:
                writer.write(str(html))
        else: print(html)



class TopLevelTag:
    def __init__(self, top_tag,  *bot_tags):
        self.top_tag=top_tag
        self.strtag="<%s>\n"%(self.top_tag)
        for tag in bot_tags:
            self.strtag += str(tag)+"\n"
        self.strtag += "</%s>"%(self.top_tag)
        

    def __str__(self):
           return str(self.strtag)  


class Tag:
    def __init__(self, tag, txt="", if_singl=True, **kwargs):
        self.tag=tag
        self.if_singl=if_singl
        self.txt=txt
        self.down_tag="<%s "%(self.tag)
        for key, val in kwargs.items():
            if "klass" in key: key = key.replace("klass","class")
            if "_" in key: key = key.replace("_","-")
            self.down_tag+="%s=\"%s\" "%(key,val)
        if self.if_singl:
            self.down_tag += "/>"
        else:
            self.down_tag+="> %s </%s>"%(self.txt, self.tag) 

    def __str__(self):
           return str(self.down_tag)  


#теги для  head
title=Tag("title", "Hello", False ) 
head=TopLevelTag("head", title)    

#теги для body
h1=Tag("h1", "Test", False, klass="main-text")
p=Tag("p", "another test", False, klass="container container-fluid klass3", id="id1")
img=Tag("img ", src="/icon.png", data_image="responsive")
div=TopLevelTag("div", p, img)
body=TopLevelTag("body",  h1, div)


html=TopLevelTag("html", head, body)



HTML(input("""Если необходимо вывести данные в файл введите \"file\" 
если достаточно вывода в консоль просто нажмите \"Enter\": """)) 

