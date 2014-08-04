#!/usr/bin/env python3

import os.path
import sys

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, StaticFileHandler, Application, url
from tornado.websocket import WebSocketHandler

class MessageBuffer(object):
    def __init__(self):
        self.messages = []
        self.sockets = set()

    def add_socket(self, sock):
        print("Client connected; socket added")
        self.sockets.add(sock)

    def remove_socket(self, sock):
        print("Client disconnected; socket removed")
        self.sockets.remove(sock)

    def add_message(self, msg):
        self.messages.append(msg);

    def send_messages(self):
        while len(self.messages):
            msg = self.messages.pop(0)
            for socket in self.sockets:
                socket.write_message(msg)

class ChatWebSocket(WebSocketHandler):
    def initialize(self, msgbuf):
        self.msgbuf = msgbuf

    def open(self):
        print("WebSocket opened")
        self.msgbuf.add_socket(self)

    def on_message(self, message):
        self.msgbuf.add_message(message)
        IOLoop.current().add_callback(self.msgbuf.send_messages)

    def on_close(self):
        print("WebSocket closed")
        self.msgbuf.remove_socket(self)

class IndexHandler(RequestHandler):
    def initialize(self, js_incl=None, css_incl=None):
        if isinstance(js_incl, str):
            self.js_incl = [js_incl]
        elif isinstance(css_incl, list):
            self.js_incl = js_incl
        else:
            raise TypeError('Expected string or list for js_incl')

        if isinstance(css_incl, str):
            self.css_incl = [css_incl]
        elif isinstance(css_incl, list):
            self.css_incl = css_incl
        else:
            raise TypeError('Expected string or list for css_incl')

    def get(self):
        self.render('index.t', css_incl=self.css_incl, js_incl=self.js_incl)

def main():
    msgbuf = MessageBuffer()
    app = Application([
        url(r'/', IndexHandler, {'js_incl':'chat', 'css_incl':'chat'}),
        url(r'/socket', ChatWebSocket, dict(msgbuf=msgbuf)),
        url(r'/css/(.*)', StaticFileHandler, {'path': 'css'}),
        url(r'/js/(.*)', StaticFileHandler, {'path': 'js'}),
    ],
    template_path='t/', autoreload=True)
    app.listen(8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
