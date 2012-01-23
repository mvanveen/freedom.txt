import re
import sys

def main():
  with open('freedom_template.txt', 'r') as file_obj:
    inp = file_obj.read()

  with open('locations.txt', 'r') as file_obj:
    locations = set(file_obj.readlines())

  name = raw_input('What is your name? ')
  if not name:
    print 'Error: Please enter a name!'
    sys.exit()

  inp = re.sub('{name}', name, inp)

  inp = re.sub(
    '{locations}',
    '\n'.join(x.replace('\n', '') for x in sorted(locations)),
    inp
  )

  location = raw_input('Where should I write file to [freedom.txt]? ')

  print
  print 'writing file...',
  with open(location or 'freedom.txt', 'w') as file_obj:
    file_obj.write(inp)
  print 'OK'

if __name__ == '__main__':
  main()
