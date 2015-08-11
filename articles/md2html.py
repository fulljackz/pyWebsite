#!/usr/bin/python3
# -*- coding: utf-8 -*-
import markdown
import sys
import codecs
import datetime
import os
import fileinput
import linecache

article = open(sys.argv[1], mode="r",encoding="utf-8")
lines = article.readlines()  
for line in lines:
	articleContent = lines[6:]

articleMetaData = []
i = 0
while i < 4:
	articleMetaData.append(lines[i].strip().split(':', 1)[1])
	i += 1

template = open("template.html", "r").read()
template = template.replace("#DATE#", str(datetime.date.today()))
template = template.replace("#AUTHOR#", articleMetaData[0])
template = template.replace("#TITLEPOST#", articleMetaData[1])
template = template.replace("#TAGS#", articleMetaData[2])
template = template.replace("#CATEGORY#", articleMetaData[3])
template = template.replace("#CONTENT#", markdown.markdown(''.join(articleContent), output_format="html5"))
template = template.replace("#YEAR#", str(datetime.datetime.today().year))
output = codecs.open(articleMetaData[1].lstrip().replace(" ", "_")+".html", "w", encoding="utf-8", errors="xmlcharrefreplace")
output.write(template)
output.close()
