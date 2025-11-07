SELECT ISBN, Tittel, Forfatter
FROM bok
ORDER BY Tittel;

SELECT u.UtlånsNr, u.ISBN, u.EksNr, u.Utlånsdato, l.Fornavn, l.Etternavn
FROM utlån u
JOIN låner l ON l.LNr = u.LNr
WHERE u.Levert = 0
ORDER BY u.Utlånsdato;

SELECT b.Tittel, COUNT(e.EksNr) AS AntallEksemplarer
FROM bok b
LEFT JOIN eksemplar e ON e.ISBN = b.ISBN
GROUP BY b.ISBN
ORDER BY b.Tittel;

/*Oppgave 3.1*/
SELECT*
FROM bok
WHERE Utgittår > 2000;

/*Oppgave 3.2*/
SELECT Forfatter, Tittel
FROM bok
ORDER BY Forfatter ASC;

/*Oppgave 3.3*/
SELECT*
FROM bok
WHERE AntallSider > 300;

/*Oppgave 3.4*/
INSERT INTO bok (ISBN, Tittel, Forfatter, Forlag, Utgittår, AntallSider)
VALUES (9788201231111, 'Doom fox', 'iceberg slim', 'cappelen damm', 2022, 300);

/*Oppgave 3.5*/
INSERT INTO låner (Fornavn, Etternavn)
VALUES ('Kenneth', 'Sheikh, Dælenenggata 40');

/*Oppgave 3.6*/
UPDATE låner
SET Adresse = 'jordstjerneveien 29'
WHERE LNr = 9;

/*Oppgave 3.7*/
SELECT u.UtlånsNr, l.Fornavn, l.Etternavn, b.Tittel, u.utlånsdato
FROM utlån u
JOIN låner l ON u.LNr = l.LNr
JOIN bok b ON u.ISBN = b.ISBN
ORDER BY u.Utlånsdato;

/*Oppgave 3.8*/
SELECT b.Tittel,COUNT(e.EksNr) AS AntallEksemplarer
FROM bok b
LEFT JOIN eksemplar e ON b.ISBN = e.ISBN
GROUP BY b.ISBN
ORDER BY b.Tittel;

/*Oppgave 3.9*/
SELECT l.Fornavn, l.Etternavn, COUNT(u.UtlånsNr) AS AntallUtlån
FROM låner l
LEFT JOIN utlån u ON l.LNr = u.LNr
GROUP BY l.LNr
ORDER BY AntallUtlån DESC;

/*Oppgave 3.10*/
