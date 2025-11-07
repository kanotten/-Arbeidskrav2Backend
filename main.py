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


if __name__ == "__main__":
    conn = connect_to_database()
    print("Database connection established.\n")
    vis_alle_bøker(conn)
    conn.close()
