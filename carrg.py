from pystyle import Colorate, Colors

import time, banners, os

import cores as c

def carrg():

 os.system('clear')

  

 print(Colorate.Vertical(Colors.green_to_blue, banners.banner2))

 print(f'\nCarregando {c.bgreen}FK{c.white}...')

 time.sleep(3)
