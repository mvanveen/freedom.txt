import re
import socket
import sys
from urlparse import urlparse

import yaml

def main():
  with open('freedom_template.txt', 'r') as file_obj:
    inp = file_obj.read()

  with open('locations.txt', 'r') as file_obj:
    user_locations = set(file_obj.readlines())

  with open('poi.txt', 'r') as file_obj:
    poi_locations = set(file_obj.readlines())

  name = raw_input('What is your name? ')
  if not name:
    print 'Error: Please enter a name!'
    sys.exit()

  inp = re.sub('{name}', name, inp)

  get_addrs = lambda locations: dict([(
    location,
    socket.gethostbyname(
      urlparse(location).netloc)
    ) for location in locations
  ])

  set_addrs = lambda locations: dict([(
    x.replace('\n', ''), y) for x, y in
     sorted(locations.iteritems(), key=lambda x: x[0])
  ])

  inp = re.sub(
    '{locations}',
    '---\n' + yaml.dump({
      'humans': set_addrs(get_addrs(user_locations)),
      'poi': set_addrs(get_addrs(poi_locations))
    }, default_flow_style=False )+ '---\n',
    inp
  )

  print inp
  location = raw_input('Where should I write file to [freedom.txt]? ')

  print
  print 'writing file...',
  with open(location or 'freedom.txt', 'w') as file_obj:
    file_obj.write(inp)
  print 'OK'

if __name__ == '__main__':
  main()
