from collections import defaultdict
from operator import __add__
import re
import socket
import sys
from urlparse import urlparse
from optparse import OptionParser

import yaml


parser = OptionParser()
parser.add_option('--with-hosts', dest='with_hosts', default=False, action='store_true')
parser.add_option('--hosts-file', dest='hosts_file')
parser.add_option('--write-hosts', dest='write_hosts', default=False, action='store_true')

def write_hosts(hosts=None):
  '''Writes an /etc/hosts file to a string'''
  assert isinstance(hosts, dict), 'Expected hosts var to be a dict!'
  max_len = max(
    [len(x) for x in hosts.iterkeys()] +
    reduce(__add__, [[len(ip) for ip in ips] for ips in hosts.itervalues()])
  )

  entries = []
  for domain, ips in hosts.iteritems():
    for ip in ips:
      entries.append(' '.join((ip.ljust(max_len), domain)))
  return '\n'.join(entries)


def get_hosts(hosts_txt):
  '''Parses an /etc/hosts file'''
  hosts = hosts_txt.split('\n')
  hosts = [re.sub('[\t ]*#.*', '', x.rstrip()) for x in hosts if x]
  hosts = filter(
    lambda x: x[0] and x[1],
    [tuple(re.split('[ \t]*', x)) for x in hosts]
  )

  final_hosts = defaultdict(list)

  for ip, hostname in hosts:
    final_hosts[hostname].append(ip)
  return dict(final_hosts)


def main(hosts_file='/etc/hosts', with_hosts=False, write_hosts_set=False):
  with open('freedom_template.txt', 'r') as file_obj:
    inp = file_obj.read()

  with open('locations.txt', 'r') as file_obj:
    user_locations = set(file_obj.readlines())

  with open('poi.txt', 'r') as file_obj:
    poi_locations = set(file_obj.readlines())

  with open(hosts_file, 'r') as hosts_file_obj:
    hosts_locations = hosts_file_obj.read()

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
  dump_dict = {
      'humans': set_addrs(get_addrs(user_locations)),
      'poi': set_addrs(get_addrs(poi_locations)),
    }

  if with_hosts:
    dump_dict.update({'hosts_file': get_hosts(hosts_locations)})

  inp = re.sub(
    '{locations}',
    '---\n' + yaml.dump(dump_dict, default_flow_style=False )+ '---\n',
    inp
  )

  print inp
  location = raw_input('Where should I write file to [freedom.txt]? ')

  print
  print 'writing file...',
  with open(location or 'freedom.txt', 'w') as file_obj:
    file_obj.write(inp)
  print 'OK'

  if write_hosts_set:
    print 'writing file [HOSTS]...',
    with open('HOSTS', 'w') as file_obj:
      output_dict = get_hosts(hosts_locations)

      make_list_dict = lambda old_dict: [(urlparse(x).netloc, [y]) for x, y in old_dict.iteritems()]

      output_dict.update(make_list_dict(dump_dict['poi']))
      output_dict.update(make_list_dict(dump_dict['humans']))

      file_obj.write(write_hosts(output_dict))

    print 'OK'

if __name__ == '__main__':
  (options, args) = parser.parse_args()
  main(
    options.hosts_file or '/etc/hosts',
    with_hosts=options.with_hosts,
    write_hosts_set=options.write_hosts
  )
