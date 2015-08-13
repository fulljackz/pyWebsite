# pyWebsite
Little script to generate static website and article part

## How to use ?
Just go to articles folder, write .md file and exec script :

./md2html.py 

Script use metadata, you can replace all needed in your markdown file copied from articleTemplate.md.

Article link will be based on workingDir variable.

For each script iteration, all articles (for the moment) are converted to html and ./articles/index.html is built to print articles abstracts.

Inspired from : https://github.com/Konosprod/pySimpleMkSite 
