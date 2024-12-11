import socket
from sql.def_all_sql import inject_ip_all
from sql.def_all_sql import inject_ip_censored
import pandas as pd
import dns.resolver



def ip_domain_socket(domain):

    try:
        
        ip_address = socket.gethostbyname(domain)
        inject_ip_all(ip_address, domain)
    except socket.error as e:
        return 


def read_domain_fr():
    csv_file = "domains_fr.csv"
    df = pd.read_csv(csv_file, sep=";")
    domains = df['domain_nom']


def query_dns(domain):
    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['194.2.0.50']  # Spécifier un serveur DNS (par exemple, Google DNS)
    
    try:
        answer = resolver.resolve(domain, 'A') 
        
        return [rdata.address for rdata in answer]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        
        return None  
    except Exception as e:
        
        return None


def is_censored(domain):

    dns_ip = '8.8.8.8'
    
    rep = ip_check(domain)
    

    reponse = query_dns(domain)
    print(reponse)
    
    if reponse is None and rep is not None:
        
        return None
    else:
        
        return False 

def ip_check(domain):

    try:
        
        ip_address = socket.gethostbyname(domain)
       
        return ip_address
    except socket.error as e:
        return None