import sqlite3


def connect_to_database(db_path="ga_bibliotek.db"):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def vis_alle_bøker(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bok")
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


def register_utlan(conn, lnr, isbn, eksnr, utlansdato):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM eksemplar WHERE ISBN = ? AND EksNr = ?",
        (isbn, eksnr),
    )

    if cursor.fetchone() is None:
        print("kan ikke registrer utlån, ugyldig eksemplar")
        return

    cursor.execute('SELECT 1 FROM "låner" WHERE "LNr" = ?', (lnr,))
    if cursor.fetchone() is None:
        print("Kan ikke registrere utlån: låner finnes ikke.")
        return

    cursor.execute(
        'SELECT 1 FROM "utlån" WHERE ISBN = ? AND EksNr = ? AND Levert = 0',
        (isbn, eksnr),
    )
    if cursor.fetchnone() is None:
        print("Eksemplar lånt ut")
        return

    cursor.execute(
        'INSERT INTO "utlån" ("LNr","ISBN","EKsNr","Utlånsdato","Levert",) VALUES (?,?,?,?,0)',
        (lnr, isbn, eksnr, utlansdato),
    )
    conn.commit()
    print(f"Utlån registrert. UtlånsNr={cursor.lastrowid}")


if __name__ == "__main__":
    conn = connect_to_database()
    print("Database connection established.\n")
    vis_alle_bøker(conn)
    conn.close()
