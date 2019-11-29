import socket

from flask import Flask, request
import random, threading, webbrowser

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    _, port = tcp.getsockname()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    tcp.close()
    return IPAddr, port


if __name__ == "__main__":
    addr, port = get_free_tcp_port()
    url = 'http://{}:{}/'.format(addr, port)
    threading.Timer(1.25, lambda: webbrowser.open_new(url)).start()
    app.run(host=addr, port=port, debug=False)