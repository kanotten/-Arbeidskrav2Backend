INSERT INTO bok (ISBN, Tittel, Forfatter, Forlag, UtgittÅr, AntallSider) VALUES
('8203188443','Kristin Lavransdatter: kransen','Undset, Sigrid','Aschehoug',1920,323),
('8203209394','Fyret: en ny sak for Dalgliesh','James, P. D.','Aschehoug',2005,415),
('8205312443','Lasso rundt fru Luna','Mykle, Agnar','Gyldendal',1954,614),
('8250336148','Victoria','Hamsun, Knut','Gyldendal',1898,111),
('8253025033','Jonas','Bjørneboe, Jens','Pax',1955,302),
('8278442231','Den gamle mannen og havet','Hemingway, Ernest','Gyldendal',1952,99);

INSERT INTO eksemplar (ISBN, EksNr) VALUES
('8203188443',1),
('8203188443',2),
('8203209394',1),
('8203209394',2),
('8205312443',1),
('8250336148',1),
('8250336148',2),
('8253025033',1),
('8253025033',2),
('8278442231',1);

INSERT INTO låner (LNr, Fornavn, Etternavn, Adresse) VALUES
(1,'Lise','Jensen','Erling Skjalgssons gate 56'),
(2,'Joakim','Gjertsen','Grinda 2'),
(3,'Katrine','Garvik','Ottar Birtings gate 9'),
(4,'Emilie','Marcussen','Kyrre Grepps gate 19'),
(5,'Valter','Eilertsen','Fyrstikkbakken 5D'),
(6,'Tormod','Vaksdal','Lassons gate 32'),
(7,'Asle','Eckhoff','Kirkeveien 5'),
(8,'Birthe','Aass','Henrik Wergelands Allé 47');

INSERT INTO utlån (UtlånsNr, LNr, ISBN, EksNr, Utlånsdato, Levert) VALUES
(1,2,'8203209394',1,'2022-08-25',0),
(2,2,'8253025033',1,'2022-08-26',1),
(3,4,'8203188443',1,'2022-09-02',0),
(4,8,'8278442231',1,'2022-09-02',0),
(5,2,'8250336148',2,'2022-09-03',1),
(6,2,'8203209394',2,'2022-09-06',0),
(7,7,'8205312443',1,'2022-09-11',1);
