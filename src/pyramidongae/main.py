"""Pyramid demo app"""
from pyramid.config import Configurator
from pyramid.response import Response
from paste.httpserver import serve

from google.appengine.ext.webapp import util

def hello_world(request):
    return Response('Hello world!')

def goodbye_world(request):
    return Response('Goodbye world!')

def main():
    config = Configurator()
    config.add_view(hello_world)
    config.add_view(goodbye_world, name='goodbye')
    app = config.make_wsgi_app()
    util.run_wsgi_app(app)

if __name__ == '__main__':
    main()
