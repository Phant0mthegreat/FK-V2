from os import system

from pystyle import Colorate, Colors

import sys, random, cores as cc, banners, carrg, emails

try:

 carrg.carrg()

 while True: 

  system('clear')

  print(Colorate.Vertical(Colors.green_to_blue, banners.banner1))

  print(f"""

{cc.bgreen}[{cc.nwhite}1{cc.bgreen}] - {cc.white}Criar CPF falso

{cc.bgreen}[{cc.nwhite}2{cc.bgreen}] - {cc.white}Criar CEP falso

{cc.bgreen}[{cc.nwhite}3{cc.bgreen}] - {cc.white}Criar CNPJ falso

{cc.bgreen}[{cc.nwhite}4{cc.bgreen}] - {cc.white}Criar E-MAIL falso

{cc.bgreen}[{cc.nwhite}5{cc.bgreen}] - {cc.white}Criar IP aleatório

{cc.bgreen}[{cc.nwhite}6{cc.bgreen}] - {cc.white}Informações

{cc.bgreen}[{cc.nwhite}7{cc.bgreen}] - {cc.white}Sair\n""")

  esclh=input(f"""[{cc.bgreen}?{cc.white}] Digite a sua escolha: """)

  if esclh == '1':

   system("clear")

   print(Colorate.Vertical(Colors.green_to_blue, banners.banner3))

   print('')

   print(f"""[{cc.cyan}±{cc.white}] Gerando CPF...\n""")

   print(f"""[{cc.blue}!{cc.white}] CPF gerado com sucesso !\n""")

   print(f"""[{cc.bblue}*{cc.white}] CPF:""",random.randint(00000000000, 99999999999))

   print('')

   input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '2':  

     system("clear")

     print(Colorate.Vertical(Colors.green_to_blue, banners.banner3))

     print('')

     print(f"""[{cc.cyan}±{cc.white}] Gerando CEP...""")

     print('')

     print(f"""[{cc.blue}!{cc.white}] CEP gerado com sucesso !""")

     print('')

     print(f"""[{cc.bblue}*{cc.white}] CEP:""",random.randint(00000000, 99999999))

     print('')

     input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '3':  

     system("clear")

     print(Colorate.Vertical(Colors.green_to_blue, banners.banner3))

     print('')

     print(f"""[{cc.cyan}±{cc.white}] Gerando CNPJ...""")

     print('')

     print(f"""[{cc.blue}!{cc.white}] CNPJ gerado com sucesso !""")

     print('')

     print(f"""[{cc.bblue}*{cc.white}] CNPJ:""",random.randint(00000000000000, 99999999999999))

     print('')

     input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '4':

     system("clear")

     print(Colorate.Vertical(Colors.green_to_blue, banners.banner3))

     print('')

     print(f"""[{cc.cyan}±{cc.white}] Gerando E-MAIL...\n""")

     print(f"""[{cc.blue}!{cc.white}] E-MAIL gerado com sucesso !\n""")

     print(f"""[{cc.bblue}*{cc.white}] E-MAIL:""",random.choice(emails.email))

     print('')

     input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '5':

     system("clear")

     print(Colorate.Vertical(Colors.green_to_blue, banners.banner3))

     print('')

     print(f"""[{cc.cyan}±{cc.white}] Gerando IP...""")

     print('')

     print(f"""[{cc.blue}!{cc.white}] IP gerado com sucesso !""")

     print('')

     print(f"""[{cc.bblue}*{cc.white}] IP: {random.randint(128, 191)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 254)}""")

     print('')

     input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '6':

   system("clear")

   print(Colorate.Vertical(Colors.green_to_blue, banners.banner5))

   print(f"""{cc.white}""")

   print(f"""

[{cc.blue}i{cc.white}] Nome da ferramenta: FK\n

[{cc.blue}i{cc.white}] Versão da ferramenta: V2\n

[{cc.blue}i{cc.white}] Criador: Phant0m The Great\n

[{cc.blue}i{cc.white}] Sobre falhas/bugs: Caso encontre algum erro no sistema, entre em contato comigo (Phant0m The Great) para reportar o erro.\n

   """)

   input('[&] Aperte em [ENTER] para voltar ao menu.')

  elif esclh == '7':

   system("clear")

   print(Colorate.Vertical(Colors.green_to_blue, banners.banner4))

   print(f"""[{cc.bcyan}#{cc.white}] Até a próxima !""")

   sys.exit()

except KeyboardInterrupt:

  system("clear")

  print(Colorate.Vertical(Colors.green_to_blue, banners.banner4))

  print(f"""[{cc.bcyan}#{cc.white}] Até a próxima !""")

  sys.exit()
