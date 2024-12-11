import sqlite3


def create_table_all():
    conn = sqlite3.connect('db/' + 'all_table_domains_fr_ip.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS all_table_domains_fr_ip(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domains_nom TEXT NOT NULL,
        ip TEXT NOT NULL
    )
    """)
    conn = sqlite3.connect('db/' + 'censure_domains.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS censure_domains(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domains_nom TEXT NOT NULL,
        ip TEXT NOT NULL
    )
    """)
    conn = sqlite3.connect('db/' + 'domains_notexist.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS domains_notexist(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domains_nom TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()