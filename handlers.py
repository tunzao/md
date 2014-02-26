# coding: utf-8
class Handler:
    """
    处理从Parser调用的方法的对象
    """

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        return self.callback("start_", name);

    def end(self, name):
        return self.callback("end_", name)

	# 为什么回调函数看起来这么费劲呢
    def sub(self, name):
        def substitution(match):
            result = self.callback("sub_", name, match)
            if result is None: result = match.group(0)
            return result;
        return substitution

class HtmlRender(Handler):
    """
    用于生成html的具体处理程序

    HtmlRender内部的方法都可以通过超类的start,end, sub方法访问
    """
        
    def start_document(self):
        print "<html><head><title>...</title></head><body>"

    def end_document(self):
        print "</body></html>"

    def start_pagraph(self):
        print "<p>"

    def end_paragraph(self):
        print "</p>"

    def start_title(self):
        print "<h1>"

    def end_title(self):
        print "</h1>"

    def start_heading(self):
        print "<h2>"

    def end_heading(self):
        print "</h2>"

    def start_listitem(self):
        print "<li>"

    def end_listitem(self):
        print "</li>"
            
    def start_list(self):
        print "<ul>"

    def end_list(self):
        print "</ul>"

    def sub_emphasis(self, match):
        return "<em>%s</em>" % match.group(1)

    def sub_url(self, match):
        return "<a href='%s' >%s</a>" % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return "<a href='mailto:%s'>%s</a>" % (match.group(1), match.group(1))

    def feed(self, data):
        print data
