# Printing the bar code on a document

> In diesem Programm wird während des Druckprozesses ein Bar-Code dem Papier mitgegeben, um somit eine automatische Identifizierung zu ermöglichen. 


## Installation

### Voraussetzungen

- Linux mit Ubuntu 20.04 (Andere Distributionen wurden nicht getestet)
- CUPS (Common Unix Printer System)
- Drucker

CUPS ist als wichtiger Bestandteil bei Linux enthalten und im Browser sollte mit ```http://localhost:631/``` das Web-Interface erreichbar sein. Sollte CUPS noch nicht vorinstalliert sein, dann kann es mit ```$ sudo apt-get install cups cups-client cups-bsd``` installiert werden. Weitere Informationen zur Installation sind hier aufzufinden: https://wiki.ubuntuusers.de/CUPS/. 

Ein eingerichteter Drucker mit CUPS ist ebenfalls wichtig, da für eine erfolgreiche Ausführung des Programms der Druckertreiber modifiziert wird. *Print to PDF* wird daher **keinen Bar Code** auf dem Dokument erscheinen lassen. 


### Anleitung

Die Bestandteile, die in dieser Anleitung zu Einsatz kommen, sind in diesem Repository enthalten und können kopiert und eingefügt werden. 


**Schritt 1:** Lege die Datei ```mypdfprefilter``` im CUPS Filter-Ordner ```/usr/lib/cups/filter/``` ab. 


**Schritt 2:** Passe die Berechtigungen des Filters an, sodass sie den Berechtigungen der anderen Filter in diesem Verzeichnis gleichen: 

```bash
$ sudo chmod 755 mypdfprefilter
```


**Schritt 3:** Öffne die PPD-Datei des installierten Druckertreibers, welche sich im Verzeichnis ```/etc/cups/ppd/``` befindet, und füge oberhalb der anderen CUPS-Filtereinträge, welche mit ```*cupsFilter: … ``` gekennzeichnet sind, folgende Zeile hinzu:

```
*cupsPreFilter: "application/vnd.cups-postscript 0 mypdfprefilter"
```


**Schritt 4:** Lege die Datei ```local.types``` im Verzeichnis ```/etc/cups/``` ab und passe die Berechtigungen an, sodass diese den Berechtigungen der anderen ```*.types``` Dateien in diesem Verzeichnis gleichen.


**Schritt 5:** Stoppe und starte Cups neu um die änderungen wirksam zu machen:

```bash
$ sudo /etc/init.d/cups stop
$ sudo /etc/init.d/cups start
```

Das Programm ist nun eingereichtet und gibt den zu druckenden Dokumenten einen Bar Code mit für die automatische Identifizierung. 
