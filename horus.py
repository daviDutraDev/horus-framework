
from temple.temple_engine import *

print("""
  _   _   __                 
 | | | | /_/  _ __ _   _ ___ 
 | |_| |/ _ \\| '__| | | / __|
 |  _  | (_) | |  | |_| \\__ \\
 |_| |_|\\___/|_|   \\__,_|___/
                             
        Created by Davi Gesser Dutra
""")

dominio = input("Digite seu Dominio(ex: google.com)")

Target = TempleEngine(dominio)
Target.run_engine()
