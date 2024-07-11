# Grimstad Adressetidene Jubilant Formaterer

Dette er et script som tar jubilant data fra NTB og formaterer den til bruk i Grimstad Adressetidene. Det lar også brukeren fjerne

# 📦 For å kjøre:
Programmet kan kun kjøres med .bat filen fra Windows PCer, men kan kjøres fra terminal i Windows, Mac og Linux

### Struktur 
```
gat_jubilant_formatter-main
├── jubilant_formatter.py
├── run_windows.bat <--- Dobbelttrykk denne for å kjøre
├── 📄 Plasser uformaterte .csv fil her <----
└── 📥 GAT_jublianter.txt <---- Dette er output og genereres etter kjøring
    
```

### Stegvis

#### Førstegangs Installering
> Ikke nødvendig, men for brukbarhet anbefaler jeg å installere windows terminal: [Link](https://www.microsoft.com/store/productId/9N0DX20HK701?ocid=pdpshare)
+ Du må ha python installert lokalt på maskinen din:  [Link](https://www.python.org/downloads/)
+ Trykk på grønn `<>Code` knapp oppe til høyre, og trykk "Download ZIP"
+ Pakk ut zip filen og legg mappen tilgjengelig, f.eks på skrivebord.  

#### Kjøring
+ Legg `.csv` fil fra NTB i samme mappe.
+ Kjør (dobbelttrykk) `run_windows.bat` fil
+ Jubilanter skal nå ligge i `GAT_Jubilanter_(dato).txt`. Disse kan du nå bruke i GAT :D

> NB! Scriptet er ikke grundig testet og derfor burde det alltid dobbeltsjekkes om jubilanter er riktig! 
