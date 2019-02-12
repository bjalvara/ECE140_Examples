from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

''' Our Fake DB (should be stored in an actual database of some kind) '''
the_users = [
  {'user_info': {'name': 'Rick Gessner', 'superpower': 'C+++++'}},
  {'user_info': {'name': 'Manjot Bilkhu', 'superpower': 'Teleportation'}},
  {'user_info': {'name': 'Raul Pegan', 'superpower': 'Bolockschain'}},
  {'user_info': {'name': 'Ramsin Khoshabeh', 'superpower': 'Scooting in the Rain'}}
]

''' Routes '''
def view_route(req):
  return FileResponse('home.html')

def rest_route(req):
  the_id = int(req.matchdict['user_id'])
  return the_users[the_id]

''' Main Application '''
def main() :
  with Configurator() as config:
    # for templating
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    # view route
    config.add_route('homepage', '/')
    config.add_view(view_route, route_name='homepage')

    # rest route
    config.add_route('get_users', '/users/{user_id}')
    config.add_view(rest_route, route_name='get_users', renderer='json')

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