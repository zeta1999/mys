import re

mo = re.match('(sub)(.*)(\\d)', 'subject4')

if mo:
    print('Groups:', mo.groups())
else:
    print('No match.')
