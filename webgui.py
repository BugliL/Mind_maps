import socket

import flask
from flask import Flask, request, render_template
import random, threading, webbrowser

from graphviz import Digraph, Source

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='',
)


def render_image(text):
    graph = Source(text)
    graph.save('data/graph')
    graph.render('static/img/graph', format='png')


def read_text_from_file():
    graph = Source.from_file('data/graph')
    return graph.source.strip()


@app.route("/", methods=['GET', 'POST'])
def index():
    text = request.form.get('text', read_text_from_file())
    context = {'text': text, }
    render_image(text)
    rendered_template = render_template("index.html", **context)
    response = flask.make_response(rendered_template)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.after_request
def add_header(request):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    request.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    request.headers["Pragma"] = "no-cache"
    request.headers["Expires"] = "0"
    request.headers['Cache-Control'] = 'public, max-age=0'
    return request


if __name__ == "__main__":
    def get_free_tcp_port():
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind(('', 0))
        _, port = tcp.getsockname()
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        tcp.close()
        # return ip_addr, port
        # FIXME: Reactivate ip address and port
        return '192.168.178.56', 5555


    addr, port = get_free_tcp_port()
    url = 'http://{}:{}/'.format(addr, port)
    # threading.Timer(1.25, lambda: webbrowser.open_new(url)).start()
    app.run(host=addr, port=port, debug=False)
