#coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import mailutil
import threading,time
from conf import config

from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        report_file = self.get_argument('report')
        subject = self.get_argument('subject')

        t = threading.Timer(5000,self.mail(report_file,subject))
        t.start()
        self.write(report_file + ', friendly user!')

    def mail(self,report_file,subject):
        time.sleep(10)
        mailutil.sendEmail(config.authInfo, config.fromAdd, config.toAdd,
                   config.ccAdd, subject, config.plainText,
                   report_file, report_file)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()