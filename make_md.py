import sys
import yaml
if len(sys.argv) < 2:
    exit()

try:
    with open(sys.argv[1], encoding='utf-8') as f:
        ls = yaml.load(f)['cells']
except:
    exit()

for dc in ls:
    typ = dc['cell_type']
    src = ''.join(dc['source'])
    if not src: continue
    if typ == 'markdown':
        print('%s' % src)
    elif typ == 'raw':
        print('<pre>\n%s\n</pre>' % src)
    elif typ == 'code':
        print('\n```py3:python3\n%s\n```' % src)
