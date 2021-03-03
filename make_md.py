import sys
import yaml
if len(sys.argv) < 2:
    exit()

try:
    with open(sys.argv[1], encoding='utf-8') as f:
        ls = yaml.load(f)['cells']
except:
    exit()

md = ""
save_f = True
for i, dc in enumerate(ls):
    typ = dc['cell_type']
    src = ''.join(dc['source'])
    if not src: continue
    if typ == 'markdown':
        md += '%s' % src + "\n"
    elif typ == 'raw':
        md += '<pre>\n%s\n</pre>' % src + "\n"
    elif typ == 'code':
        md += '\n```py3:python3\n%s\n```' % src + "\n"

    if i == 0:
        file_name = sys.argv[1].split(".ipynb")[0]
        src = src.split("#")[1]
        with open("src/readme.md", "r") as f:
            lines = f.readlines()
            for l in lines:
                if file_name in l:
                    save_f = False
        if save_f:
            with open("src/readme.md", "a") as f:
                f.write("| {} | {} | [Link]() |\n".format(file_name, src))


with open("note/{}.md".format(file_name.split("/")[1]), "w") as f:
    f.write(md)
