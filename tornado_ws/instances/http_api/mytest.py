from tornado.web import RequestHandler


class MyHttp(RequestHandler):
    def get(self):
        # self.render("base.html")
        self.write("ok")
