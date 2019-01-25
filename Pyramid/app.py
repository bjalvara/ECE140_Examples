from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

''' Routes '''
def basic_route(req):
  return Response('Hello World!!!')

def view_route(req):
  return FileResponse('index.html')

def template_route(req):
  data = {'message': 'Greetings!'}
  return render_to_response('index2.html', data, request=req)

def template_route2(req):
  data = {'count': 1, 'files': ['msg1.html', 'msg2.html', 'msg3.html']}
  return render_to_response('index3.html', data, request=req)

''' Main Application '''
def main() :
  with Configurator() as config:

    # basic_route
    config.add_route('hello', '/')
    config.add_view(basic_route, route_name='hello')

    # view_route
    config.add_route('codepen_example', '/codepen')
    config.add_view(view_route, route_name='codepen_example')

    # for template_route / template_route2
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('template_example', '/template')
    config.add_view(template_route, route_name='template_example')

    config.add_route('template_example2', '/template2')
    config.add_view(template_route2, route_name='template_example2')

    # add static folder to search path
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    # create the webserver config
    app = config.make_wsgi_app()

  # run the server
  server = make_server('127.0.0.1', 8080, app)
  print("The server is now running on: http://127.0.0.1:8080")
  
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)

if __name__ == '__main__':
  main()