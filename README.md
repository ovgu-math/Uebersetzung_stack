Diese Anleitung ist zur Übersetzung von allen Fragen in einer Kategorie oder einzelner Fragon von Deutsch oder Englisch zu Mutlilang mit Deutsch und Englisch.

# Vorraussetzungen
Alle gewählten Fragen müssen zu Beginn vollständig in der selben Sprache sein und noch keine Multilang Tags enthalten.

# Limitationen
Text in CAS Feldern (Felder für Maxima code) (zb. bei Multiple-Choice-Fragen) erscheint nicht in der .csv Datei und muss manuell übersetzt werden, wie zb. "[[lang code='de']]Beispiel[[/lang]][[lang code='en']]Example[[\lang]]"
Quizzes müssen zuletzt manuell aktualisiert oder neu-erstellt werden, sodass sie die übersetzten Fragen verwenden anstelle von den alten nicht-übersetzten.

# Installation
## 1. Notwendige Software
### Installiere ein Programm zum Bearbeiten von .csv Datein
 zb. Libreoffice oder Excel

### Installiere Python und pip
#### In Windows:
 Der Installer kann von der Webseite heruntergeladen werden:  https://www.python.org/downloads/windows/
 Für mehr Info siehe:  https://learn.microsoft.com/de-de/windows/python/beginner
 Kreuze im Installer an, dass Python zum PATH hinzugefügt werden soll.
  Sonst muss es manuell zum PATH hinzugefügt werden.
   Python ist standardmäßig unter "%ProgramFiles%\Python X.Y" oder "%ProgramFiles(x86)%\Python X.Y" oder "%LocalAppData%\Programs\Python\PythonXY" oder "%LocalAppData%\Programs\Python\PythonXY-32" oder "%LocalAppData%\Programs\Python\PythonXY-64" installiert.  (ersetze X.Y durch die installierte Python version)
   Um PATH zu ändern:
    Öffne regedit.exe
    Navigiere zu: "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    Wenn der Wert von PATH bereits den Pfad zur Python Installation (zb. "C:\Program Files\Python312\") enthält muss es nicht mehr hinzugefügt werden.
    Ansonsten füge hinten an den Wert der Variable PATH ein ";" an und danach den Pfad zu der Python Installation.
     Danach füge hinten an den Wert der Variable PATH ein ";" an und danach den Pfad zu den "Script" Ordner in der Python Installation.
     Der Wert der PATH variable sollte danach ungefähr wie folgt aussehen: "%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\system32\wbem;%SystemRoot%\system32\WindowsPowershell\v1.0;C:\Program Files\dotnet\;C:\Program Files\Python312\;C:\Program Files\Python312\Scripts\"
####  In Linux und Mac
 kann Python und pip einfach mit den Package Manager bzw. App Store installiert werden.

### Installiere Docker
#### in Windows
Der Installer kann von www.docker.com heruntergeladen werden.
#### in Linux und Mac
Docker kann von den Package Manager bzw. App Store installiert werden.

### Validiere
 dass das alles richtig installiert ist, indem Sie CMD, oder eine Shell im Terminal öffnen und den Befehl "python --version" und "pip --version" und "docker --version" eingeben.
 Die Befehle sollten dann die installierten Versionen von Python und pip und docker ausgeben.


### Installiere lxml, und beautifulsoup4 mit pip
#### Befehle:
 "pip install lxml"
 "pip install beautifulsoup4"
#### In Linux und Mac
 können manche von diesen auch mit den Package Manager bzw. App Store installiert werden.

### Installiere libretranslate mit Docker
#### Befehl:
 "docker run -p 5000:5000 -it --net=host --name libretranslate libretranslate/libretranslate --load-only de,en"\
Der Selbe Befehl wird verwendet um Libretranslate zu starten und auszuführen\
Warte bis es sagt: "Running on http://*:5000"
#### Validiere
dass es richtig installiert ist indem Sie im Webbrowser "localhost:5000" öffnen.\
Wenn es richtig funktioniert, sollten Sie die libretranslate Webseite sehen.


## 2. Export der Fragen aus Moodle
1. Navigiere zu den Moodle Kurs.
1. In der Top-bar, klicke auf das Zahnrad, dann im Menu klicke auf "Mehr".
1. Dann neben "Fragensammlung" klicke auf Export und wähle "Moodle-XML-Format" als Dateiformat und klicke "Fragen in Datei exportieren"
1. Es startet dann ein Download für die .xml Datei.
1. In Windows: aktiviere Dateinamenerweiterungen, wie nach:  https://support.microsoft.com/de-de/windows/allgemeine-dateierweiterungen-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01

## 3. Vorbereitung für die Übersetzung
1. Erstelle ein Ordner für die Übersetzung. 
1. Kopiere die .xml Datei in den Ordner.
1. Kopiere die Python-scripte(.py Datein) in den Ordner.
1. Navigiere zu den Ordner in CMD oder in einer Shell mithilfe von den "cd" Befehl, oder den File Explorer. (Alle Befehle müssen in diesen Ordner ausgeführt werden.)
    * Im File Explorer: Öffne den Ordner, und dann mit ein rechts-Klick im Ordner öffnet sich ein Menu, in den Menu klicke "Im Terminal öffnen" oder etwas ähnliches.
    * In CMD:\
    Mit den "dir" Befehl können alle Datein und Ordner(als \<DIR\> markiert) gelistet werden.
    * In einer POSIX-compliant Shell (zb. Windows Powershell, oder Bash)\
  Mit den "ls" Befehl können alle Datein und Ordner gelistet werden.\
  Mit den "ls -d" Befehl können alle Ordner gelistet werden.
    * Generell:\
  Mit "cd \[Name des Ordner\]" kann zu den Ordner navigiert werden.\
  Mit "cd .." kann man zu den Obergeordneten obergeordneten Ordner zurück navigieren.

## 4. Übersetzung
Gebe den Befehl "python helper" ein und folge die Anweisungen.


## 5. Import in Moodle
1. Geben Sie den Befehl "python fix_template.py" ein.
1. Geben Sie den Befehl "python csv2xml.py" ein.
* Es wird dann eine neue _new.xml Datei im Ordner erstellt.
1. Dann in Moodle, im selben Menu wo "Export" stand neben "Fragensammlung", klicke auf "Import".
1. Wähle "Moodle-XML-Format" als Dateiformat und die _new.xml Datei als Datei.
1. Dann klicke Import.

Die Frage werden in einer Neuen Unterkategorie namens "übersetzt" importiert, wenn die xml-Datei die Kategorien beinhaltete.
Davon abgesehen bleibt die Kategorienstruktur erhalten.
Die alten Fragen bleiben unverändert.

## 6. Aktualisiere Quizzes und CAS-Felder
Alle Quizze werden danach noch die alten Fragen referenzieren.
Daher müssen entweder alle Quizzes neu erstellt werden mit den neuen Fragen.
Oder von allen Quizzen müssen alle Fragen entfernt werden und mit den übersetzten Fragen ersetzt werden.
Text unter "Questionvariables" oder "Aufgabenvariablen" wird nicht in der .csv Datei zum Übersetzen auftauchen. Daher muss der Text noch manuell übersetzt werden.
Hierfür kann die Maxima-Funktion " tr(de,en):=castext("\[\[lang code='de'\]\]{@de@}\[\[/lang\]\]\[\[lang code='en'\]\]{@en@}\[\[/lang\]\]"); "  hilfreich sein. Sie wird wie folt aufgerufen:  " tr("Beispiel","Example") ".

## 7. (optional) Hochladen der Fragen in Git
zum Teilen mit anderen Universitäten
Geben Sie den Befehl "python prettyfy_cli \[Name der _new.csv Datei\]" und danach "python split_exported_xml \[Name der _new.csv Datei\]" ein.
Es sollte dann ein neuer Ordner namens "separate_questions" erscheinen mit allen Fragen als separate .xml Datein.
Diese .xml Datein können dann in ein Git Repository hochgeladen werden.





