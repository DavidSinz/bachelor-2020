# Using Printed Bar Codes to Link Physical Documents to Digital Files

- Betreuer: Andreas Schmid

- Bearbeiter: David Sinz

- Erstgutachter: Raphael Wimmer

- Wiki: https://wiki.mi.ur.de/arbeiten/barcode_print

## Hintergrund

> Diese Projekt bildet eine Brücke zwischen der digitalen und der physikalischen Welt, indem es eine Verlinkung zwischen ausgedruckten Dokumenten und deren digitalen ursprünglichen Dateien herstellt. 

## Zielsetzung

Das Hybrid Document Management beschäftigt sich mit Verfahren und Technologien, um eine Brücke zwischen Papier und digitalen Dateien zu schlagen. Dies stößt auf gewisse Hindernisse und Herausforderungen, da ein Blatt Papier keine elektronischen Features besitzt auf denen Informationen und Identifizierungsmerkmale gespeichert werden können. Dokumente, die ausgedruckt werden, verlieren alle ihre digitalen Merkmale, wie zum Beispiel:

- Dateienname
- Speicherort
- Text -und Bildeigenschaften
- Metadaten (Author, Titel, Datum etc)

Um diesen Informationsverlust entgegen zu wirken, beschäftigt sich dieses Projekt mit einem Lösungsansatz, bei welchem ein Bar Code dem zu druckendem Dokument mitgegeben wird und somit eine Verlinkung zu den digitalen Informationen bestehen bleibt. 

## Komponenten

Um eine robuste und funktionierende Umsetzung des Programms durchzuführen, werden existierende Systeme und Programmbibliotheken gewählt. Im Folgendem werden diese aufgezählt:

1. Betriebssystem: Linux (Ubuntu 20.04)
2. Druckerprogramm: Common Unix Printer System (CUPS)
3. Programmiersprachen: Python 3.8, Shellskriptsprache

Des Weiteren werden folgende Libraries verwendet, diese können jedoch im weiteren Projektverlauf variieren: *ghostscript*, *qrencode*.

