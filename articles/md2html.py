#!/usr/bin/python3
# -*- coding: utf-8 -*-
import markdown
import sys
import codecs
import datetime
import os
import fileinput

# Open arg file and parse lines by lines
article = open(sys.argv[1], mode="r",encoding="utf-8")
lines = article.readlines()  

# Set article content from line 7 to eof
for line in lines:
	articleContent = lines[6:]

# Set metadata to list
articleMetaData = []
i = 0
while i < 4:
	articleMetaData.append(lines[i].strip().split(':', 1)[1])
	i += 1

# Replace tags in template with metadata
template = open("template.html", "r").read()
template = template.replace("#DATE#", str(datetime.date.today()))
template = template.replace("#AUTHOR#", articleMetaData[0])
template = template.replace("#TITLEPOST#", articleMetaData[1])
template = template.replace("#TAGS#", articleMetaData[2])
template = template.replace("#CATEGORY#", articleMetaData[3])
template = template.replace("#CONTENT#", markdown.markdown(''.join(articleContent), output_format="html5"))
template = template.replace("#YEAR#", str(datetime.datetime.today().year))

# Create html file with metadata title + html
output = codecs.open(articleMetaData[1].lstrip().replace(" ", "_")+".html", "w", encoding="utf-8", errors="xmlcharrefreplace")

# Write file
output.write(template)
output.close()
