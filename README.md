# -Arbeidskrav2Backend
SQL database med lån, registrering og innlevering av bøker. inkludert et bibliotek

# ga_bibliotek database
Dette dokumentet viser et lite biblioteksystem.
Den har oversikt over alle bøker, låner, utlån, eksemplarer av hver bok og viser hvordan alt henger sammen.

# Verktøy
Oppgaven er laget for å bruke MySQL, men siden jeg har for gammel programvare så bruker jeg en SQlite versjon
denne verjsonen bruker samme syntax og fungerer på samme måte, men bruker terminal for å visualisere dataene.

## 1. Tabellstrukturer
Databasen består av de 4 tabellene : bok, låner, utlån, eksemplar:

-**bok**: inneholder informasjon om selve boken eller bøkene med (tittel, forfatter, år, forlag, sider, isbn osv).

-**eksemplar**: viser antall kopier av hver bok.

-**låner**: inneholder informasjon om låneren med (navn og adresse).

-**utlån**: Registrer hvert enkelt utlån og kobler det med lån, bok og eksemplarer.

Under er et detalsjert eksempel på tabellene.
### eksemplar
-**ISBN**:TEXT, NOT NULL, FOREIGN KEY → bok(ISBN) – peker til boka eksemplaret tilhører.
-**EksNr**:INTEGER, NOT NULL, PRIMARY KEY - samme isbn nummer men unikt eksemplar nr av samme bok
-**Antall**: Viser bare hvor mange antall det er av en bok.

## LÅNER
-**LNr**:INTEGER, PRIMARY KEY, AUTOINCREMENT - unikt lånenr som går automatisk.
-**Navn**:TEXT, NOT NULL - Låners fornavn.
-**Etternavn**: TEXT, NOT NULL - Låners etternavn.
-**Adresse**: TEXT, NOT NULL - Låners adresse.

## UTLAN
-**UtlNr**:INTEGER, PRIMARY KEY, AUTOINCREMENT - unikt utlån nummer som går automatisk.
-**LNr**:INTEGER, NOT NULL, FOREIGN KEY → låner(LNr) – peker til låneren som låner.
-**ISBN**:TEXT, NOT NULL, FOREIGN KEY → bok(ISBN) – peker til boka som lånes.
-**EksNr**:INTEGER, NOT NULL, FOREIGN KEY → eksemplar(EksNr) – peker til eksemplaret som lånes.
-**Levert**:INTEGER, CHECK (Levert IN (0, 1) viser om boken er levert eller ikke med et boolean verdi.


## UTRYKK
Her går vi over utrykk som vi bruker i tabellene for å sette de opp slik at det blir korrekt. at bøker og lånere samt utlån ikke duplikerer o.l.

## 2. Primærnøkler og Fremmednøkler.
**Primærnøkler**: er identfikatorer som er unikt for hver rad i en tabell.
**Fremmednøkler**: er identfikatorer som kobler sammen tabeller og sikrer at dataene henger sammen.

bok.ISBN - unikt nummer for hver bok (primærnøkkel)
eksemplar.ISBN - peker til det unike eksemplaret av boka ISBN nr tilhører (Fremmednøkkel)
