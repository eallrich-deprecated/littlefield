import os

template_header = """<html>
<head><title>Littlefield Charts</title></head>
<body>
<table>"""

template_footer = """</table>
</body>
</html>"""

root = os.path.abspath(os.path.dirname(__file__))
os.chdir(root) # Just to make sure

files = os.listdir(os.getcwd())
charts = [f for f in files if f.endswith('.png')]
charts.sort()

img_tags = []
for c in charts:
    img = "<tr><div style=\"text-align: center; background: #8EC5EF;\">%s</div><img src=\"%s\" /></tr>" % (c[:-4], c)
    img_tags.append(img)

rows = '\n'.join(img_tags)

template = "%s%s%s" % (template_header, rows, template_footer)

with open('index.html', 'wb') as f:
    f.write(template)

