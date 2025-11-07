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
