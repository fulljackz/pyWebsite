#!/usr/bin/python3
# -*- coding: utf-8 -*-
import markdown
import sys
import codecs
import datetime
import os
import fileinput
import re

workingDir = "./"
now = datetime.date.today()
path = workingDir + str(now.year)

def printHelp():
	print("Usage : ./md2html.py") 

def main():
	if len(sys.argv) > 1:
		printHelp()
		return
	buildIndex()
	buildArticle(buildIndex())


def buildArticle(article):
	#~ os.makedirs(path, exist_ok=True)
	if not article :
		print("No file was returned from buildIndex function")
	# Can not assign readlines() to articles (already open ?)
	# So write article content to temprorary file and parse it line by line to write content.
	f = open("temp", mode="w")
	f.write(article)
	f.close()
	article = open("temp", mode="r",encoding="utf-8")
	lines = article.readlines()
	# Set article content from line 7 to eof
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
	artLink = (path + "/" + articleMetaData[1].lstrip().replace(" ", "_") + ".html")
	# Create html file with metadata title + html
	output = codecs.open(artLink, "w", encoding="utf-8", errors="xmlcharrefreplace")
	# Write file
	output.write(template)
	output.close()
	os.remove("temp")
	return artLink

def buildIndex():
	abstractList = []
	# Build index with articles abstract
	for file in os.listdir(workingDir):
		if file.endswith(".md"):
			infile = open(workingDir + file,mode="r").read()
			abstracts = re.search(r'<!---Abstract(.*?)Abstract-->',infile,re.DOTALL)
			more = re.search(r'<!---Meta(.*?)Meta-->',infile,re.DOTALL)
			abstractList.append(abstracts.group(1))
			abstractList.append("<a href=" + (buildArticle(infile)+ ">read more</a>"))
	index = open("index_template.html", "r").read()
	output = codecs.open((workingDir + "index.html"), "w", encoding="utf-8", errors="xmlcharrefreplace")
	abstractString = ''.join(abstractList)
	abstractString = markdown.markdown(abstractString, output_format="html5")
	index = index.replace("#ARTICLE-SUMMARY#", abstractString)
	output.write(index)
	output.close()
	#~ os.remove("temp")
	return infile


if __name__ == "__main__":
	main()
	

	
