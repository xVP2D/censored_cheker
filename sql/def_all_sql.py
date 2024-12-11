import sqlite3

def inject_ip_all(ip_address, domain):
    domain = domain
    

    conn = sqlite3.connect('db/' + 'all_table_domains_fr_ip.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO all_table_domains_fr_ip (ip, domains_nom) VALUES (?, ?)" , (ip_address, domain))
    conn.commit()

def inject_ip_censored(ip_address, domain):
    domains = domain
    
    conn = sqlite3.connect('db/' + 'censure_domains.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO censure_domains (ip, domains_nom) VALUES (?, ?)" , (ip_address, domains))
    conn.commit()


def inject_notexist(domain):
    domains = domain
    
    conn = sqlite3.connect('db/' + 'domains_notexist.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO domains_notexist (domains_nom) VALUES (?)" , (domains,))
    conn.commit()