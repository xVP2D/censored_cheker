from sql.create_table_all import create_table_all
from python.request import ip_domain_socket
from python.request import is_censored
from sql.def_all_sql import inject_ip_censored
from sql.def_all_sql import inject_notexist
from python.request import ip_check
import pandas as pd


while True :
   
   create_table_all()
   
   domain = input("Entrez un domaine : ")
   responses = []
   rep = ip_check(domain)
   
   if rep is not  None:
       ip_domain_socket(domain)
       print(f"{domain} existe")
       if is_censored(domain) is None:
           inject_ip_censored(rep, domain)
           print(f"{domain} est censuré")
       else:
           print(f"{domain} n'est pas censuré")
   else: 
       inject_notexist(domain)
       print(f"{domain} n'existe pas")
         