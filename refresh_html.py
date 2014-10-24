import datetime
import os

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

template_header = """<html>
<head><title>Littlefield Charts</title></head>
<body>
<p>Data last collected: %s</p>
<table>""" % now

template_footer = """</table>
<p><a href="production.csv">Download production data</a></p>
<p><a href="rankings.csv">Download latest rankings</a></p>
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

