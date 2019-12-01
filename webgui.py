import socket

from flask import Flask, request, render_template
import random, threading, webbrowser

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='',
)


@app.route("/")
def index():
    return render_template("index.html")


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    _, port = tcp.getsockname()
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    tcp.close()
    # return ip_addr, port
    return '192.168.178.56', 5555


if __name__ == "__main__":
    addr, port = get_free_tcp_port()
    url = 'http://{}:{}/'.format(addr, port)
    # threading.Timer(1.25, lambda: webbrowser.open_new(url)).start()
    app.run(host=addr, port=port, debug=False)
