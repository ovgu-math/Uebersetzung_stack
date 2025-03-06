import subprocess

def pe(c,a=""):
    print("> python "+c+" "+a)
    if not a:
        subprocess.run(["python",c])
    else:
        subprocess.run(["python",c,a])
        
    
print("Wähle eine Ausgangssprache: de (Deutsch) oder en (Englisch)")
sprache=input()
if not sprache:
    sprache="de"
if sprache not in ["de","en"]:
    print("Sprache nicht erkannt")
    exit()
pe("xml2csv.py",sprache)
pe("autotranslate.py",sprache)
pe("csv4excel.py")
print("Bitte bearbeite jetzt die .xml.csv Datei (zb. mit Excel oder Libreoffice)")
print("Drücke danach die Entertaste um fortzufahren")
input()
pe("csv2xml.py")
print("fertig")
