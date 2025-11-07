import sqlite3


def connect_to_database(db_path="ga_bibliotek.db"):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def vis_alle_bøker(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bok;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def sok_bok(conn, sokeord):
    cursor = conn.cursor()
    pattern = f"%{sokeord}%"
    cursor.execute(
        """
        SELECT ISBN, Tittel, Forfatter
        FROM bok
        WHERE lower(Tittel) LIKE lower(?)
           OR lower(Forfatter) LIKE lower(?)
        """,
        (pattern, pattern),
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def registrer_utlan(conn, lnr, isbn, eksnr, utlansdato):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM eksemplar WHERE ISBN = ? AND EksNr = ?",
        (isbn, eksnr),
    )
    if cursor.fetchone() is None:
        print("Kan ikke registrere utlån: eksemplaret finnes ikke.")
        return
    cursor.execute('SELECT 1 FROM "låner" WHERE "LNr" = ?', (lnr,))
    if cursor.fetchone() is None:
        print("Kan ikke registrere utlån: låner finnes ikke.")
        return
    cursor.execute(
        'SELECT 1 FROM "utlån" WHERE ISBN = ? AND EksNr = ? AND Levert = 0',
        (isbn, eksnr),
    )
    if cursor.fetchone() is not None:
        print("Eksemplaret er allerede utlånt.")
        return
    cursor.execute(
        'INSERT INTO "utlån" ("LNr","ISBN","EksNr","Utlånsdato","Levert") VALUES (?,?,?,?,0)',
        (lnr, isbn, eksnr, utlansdato),
    )
    conn.commit()
    print(f"Utlån registrert. UtlånsNr={cursor.lastrowid}")


def lever_bok(conn, isbn, eksnr):
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE "utlån" SET Levert = 1 WHERE ISBN = ? AND EksNr = ? AND Levert = 0',
        (isbn, eksnr),
    )
    conn.commit()
    if cursor.rowcount == 0:
        print("Ingen registrerte utlån for dette eksemplaret.")
    else:
        print("Bok levert.")


def vis_lanerhistorikk(conn, lnr):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT l.Fornavn, l.Etternavn, l.Adresse,
               b.Tittel, b.Forfatter,
               u.Utlånsdato,
               CASE WHEN u.Levert = 1 THEN 'Levert' ELSE 'Utlånt' END AS Status
        FROM "låner" l
        JOIN "utlån" u ON l.LNr = u.LNr
        JOIN bok b ON b.ISBN = u.ISBN
        WHERE l.LNr = ?
        """,
        (lnr,),
    )
    rows = cursor.fetchall()
    if not rows:
        print("Ingen utlån for denne låneren.")
        return
    print(f"\nUtlånshistorikk for låner {lnr}:")
    for row in rows:
        print(row)


if __name__ == "__main__":
    conn = connect_to_database()
    print("Database connection established.\n")

    print("== Alle bøker ==")
    vis_alle_bøker(conn)

    print("\n== Søk: 'fyret' ==")
    sok_bok(conn, "fyret")

    print("\n== Registrer utlån ==")
    registrer_utlan(conn, 9, "8203209394", 1, "2025-11-07")

    print("\n== Lever bok ==")
    lever_bok(conn, "8203209394", 1)

    print("\n== Lånerhistorikk ==")
    vis_lanerhistorikk(conn, 9)

    conn.close()
