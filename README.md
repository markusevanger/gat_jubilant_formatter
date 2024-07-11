# Grimstad Adressetidene Jubilant Formaterer

Dette er et script som tar jubilant data fra NTB og formaterer den til bruk i Grimstad Adressetidene. 

# 📦 For å kjøre:
Programmet kan kun kjøres med .bat filen fra Windows PCer, men kan kjøres fra terminal i Windows, Mac og Linux

### Struktur 
```
gat_jubilant_formatter-main
├── jubilant_formatter.py
├── run_windows.bat <--- Dobbelttrykk denne for å kjøre
│
├── 📄 Plasser uformaterte .csv fil her <----
│
└── 📥 GAT_jublianter.txt <---- Denne er output og genereres etter kjøring
    
```

### Stegvis
+ Ha python installert lokalt på maskinen din: https://www.python.org/downloads/
+ Trykk på grønn `<>Code` knapp oppe til høyre, og trykk "Download ZIP"
+ Pakk ut zip filen.  
+ Legg filer som skal formateres inn i "unformatted" mappen.
+ Kjør (dobbelttrykk) vedlagt .bat fil
+ Jubilanter skal nå ligge i `GAT_Jubilanter-(dato).txt`. Disse kan du nå bruke i GAT :D

> NB! Scriptet er ikke grundig testet og derfor burde det alltid dobbeltsjekkes om jubilanter er riktig! 
