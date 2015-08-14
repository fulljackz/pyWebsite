#!/usr/bin/python3
# -*- coding: utf-8 -*-
import markdown
import sys
import codecs
import datetime
import os
import fileinput
import re

# Folder which will contain articles
buildDir = "/var/www/website/articles/"

# Folder where markdown files will be stored
mdDir = "./md_files/"

html_Dir = "./html_templates/"

# Init abstractList as list
abstractList = []

def printHelp():
	print("Usage : ./md2html.py article.md") 

def main():
	if len(sys.argv) != 2:
		printHelp()
		return
	# Open arg file and parse lines by lines
	try:
		article = open(sys.argv[1], mode="r",encoding="utf-8")
	except IOError:
		print(sys.argv[1] + " doesn't exists.")
		return
	lines = article.readlines()  
	# Set article content from line 7 to eof
	articleContent = lines[7:]
	# Set metadata to list
	articleMetaData = []
	i = 0
	while i < 5:
		articleMetaData.append(lines[i].strip().split(':', 1)[1])
		i += 1
	# Replace tags in template with metadata
	template = open(html_Dir + "template.html", "r").read()
	template = template.replace("#DATE#", articleMetaData[2])
	template = template.replace("#AUTHOR#", articleMetaData[0])
	template = template.replace("#TITLEPOST#", articleMetaData[1])
	template = template.replace("#TAGS#", articleMetaData[3])
	template = template.replace("#CATEGORY#", articleMetaData[4])
	template = template.replace("#CONTENT#", markdown.markdown(''.join(articleContent), output_format="html5"))
	template = template.replace("#YEAR#", str(datetime.datetime.today().year))
	output = codecs.open(buildDir + articleMetaData[1].lstrip().replace(" ", "_"), "w", encoding="utf-8", errors="xmlcharrefreplace")
	# Write file
	output.write(template)
	output.close()
	# Build index with articles abstract
	for file in os.listdir(mdDir):
		if file.startswith(".tmp"):
			os.remove(".tmp")
		if file.endswith(".md"):
			infile = open(mdDir + file,mode="r", encoding="utf-8").read()
			# Can not assign readlines() to infile (already open ?)
			# Write article content to temporary file, parse line by line to get article title.
			f = open(".tmp", mode="w")
			f.write(infile)
			f.close()
			tmpFile = open(".tmp", mode="r",encoding="utf-8")
			l = tmpFile.readlines()
			articleTitle = (l[1].strip().split(':', 1)[1].lstrip().replace(" ", "_"))
			abstracts = re.search(r'<!---Abstract(.*?)Abstract-->',infile,re.DOTALL)
			abstractList.append(abstracts.group(1))
			abstractList.append("<a href=" + articleTitle + ">read more</a>")
			# Delete temp created file for next iteration
			os.remove(".tmp")
	index = open(html_Dir + "index_template.html", "r").read()
	output = codecs.open((buildDir + "index.html"), "w", encoding="utf-8", errors="xmlcharrefreplace")
	abstractString = ''.join(abstractList)
	abstractString = markdown.markdown(abstractString, output_format="html5")
	index = index.replace("#ARTICLE-SUMMARY#", abstractString)
	output.write(index)
	output.close()
	return infile
	
if __name__ == "__main__":
	main()
