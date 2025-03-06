#!/usr/bin/python

import glob
#import xml.etree.ElementTree as ET
from lxml import etree as ET
from bs4 import BeautifulSoup
import csv
from bs4.formatter import HTMLFormatter
import os.path
import sys

class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            if k == 'm':
                continue
            yield k, v

filenames=glob.glob('*.xml')
fieldnames=["Nummer","de","en"]

sourceLang=sys.argv[1] if len(sys.argv)>1 and sys.argv[1] in ["de","en"] else "de"
print("Übersetzung von "+sourceLang)

for filename in filenames:
    if filename.endswith("_new.xml"):
        continue
    if os.path.isfile(f"{filename}.template") or os.path.isfile(f"{filename}.csv"):
        print(f"{filename} wird übersprungen")
        continue
    print(filename)
    tree = ET.parse(filename)
    root = tree.getroot()
    texte=root.findall('.//*[@format="html"]/text')

    groups=[]
    texts=[]
    infile=open(filename,encoding='utf8')
    inhalt=infile.read()
    infile.close()

    categories=[i.text for i in root.findall('.//question[@type="category"]/category/text')]
    if categories:
        category=os.path.commonpath(categories)
        print(f"Neue Fragen stehen unter: {category}/übersetzt")
    
        inhalt=inhalt.replace(category,category+"/übersetzt")
        inhalt=inhalt.replace('<quiz>',f"""<quiz>
<!-- question: 0  -->
  <question type="category">
    <category>
      <text>{category}</text>
    </category>
    <info format="moodle_auto_format">
      <text></text>
    </info>
    <idnumber></idnumber>
  </question>""",1)
    
    number=0
    for text in texte:
        if text.text:
            orig=text.text
            textA="<text>![CDATA["+orig+"]]></text>"
            textB="<text>"+orig+"</text>"

            if textA in inhalt:
                t=textA
            elif textB in inhalt:
                t=textB
            else:
                print(f"Fehler bei Nummer: ###{number+1}###")
                continue
            
            number+=1
            inhalt=inhalt.replace(t,"<text>![CDATA[###"+str(number)+"###]]></text>",1)
            text.text='<span class="multilang" lang="de">'+orig+'</span>'
            soup = BeautifulSoup(text.text,'html.parser')
            spans = soup.findAll("span",{"class":"multilang"})
            group=[]
            for span in spans:
                group.append(span)
                try:
                    nexttag_name=span.find_next_sibling().name
                except:
                    nexttag_name=""
            if group:
                groups.append(group)
                texts.append(orig)
                group=[]

    csvfile=open(filename+'.csv','w',newline='',encoding='utf8')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    number=0
    for group in groups:
        number+=1
        zeile={sourceLang:texts[number-1]}
        zeile['Nummer']='###'+str(number)+'###'
        writer.writerow(zeile)
    csvfile.close()

    templatefile=open(filename+'.template','w',encoding='utf8')
    inhalt=inhalt.replace('<text>###','<text><![CDATA[###')
    inhalt=inhalt.replace('###</text>','###]]></text>')
    templatefile.write(inhalt)
    templatefile.close()

