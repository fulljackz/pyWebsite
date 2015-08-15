# pyWebsite
Little script to generate static website and article part

## Archive content
Script runs with a single argument each times.

Archive contains multiples files :
 * html_templates : contain html files which are used to build web pages
 * md_files : contain markdown files which are transformed to html for publish content
 * index.html : simple web page to place in root web folder
 * md2html.py : script to transform markdown to html
 * css : folder which contains simple css file to make simple but easy readable website.

## Few notes :

Script contains 3 "important" variables :

 * buildDir : is reception folder var for html built files (ie : /var/www/articles/ )
 * mdDir : is markdown storage folder. Store all of your articles here. Template is available for example.
 * html_Dir : is template folder var for html template files (ie : ./html_templates )
 * Script use markdown and pygments lib. You can install them with :
```
pip3 install markdown Pygments
``` 

## How it works ?

Just go to repo folder, write .md files in mdDir and exec script :

```
./md2html.py mdDir/your_file.md
```

Script use metadata, you can replace all needed in your markdown file copied from articleTemplate.md.

Article link will be based on article name

For each script iteration (for a new article), markdown related file is processed and articles/index.html is regenerated to use latest article.

Inspired by : https://github.com/Konosprod/pySimpleMkSite 
