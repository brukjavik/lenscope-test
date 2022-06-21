### CAPTAÇAO DOS PARAMETROS DO USUARIO ###

geoe = float(input("Digite o valor para o grau esferico do olho esquerdo: "))
geod = float(input("Digite o valor para o grau esferico do olho direito: "))
gcoe = float(input("Digite o valor para o grau cilindrico do olho esquerdo: "))
gcod = float(input("Digite o valor para o grau cilindrico do olho direito: "))

flag = 0 # Criacao de uma variavel de controle

### CHECAGEM: LENTE ###

if(gcoe==0 and gcod==0): # Verifica se o usuario possui algum grau cilindrico
    if((geoe<=-3 and geoe>=-12) and (geod<=-3 and geod>=-12)): # Analisa as condicoes para o uso da lente prime
        print("Recomenda-se a lente prime")
    elif((geoe<=-0 and geoe>=-15) and (geod<=-0 and geod>=-15)): # Analisa as condicoes para o uso da lente vision
        print("Recomenda-se a lente vision")
    else: print("Nao ha nenhuma lente disponivel no momento") # Caso nenhuma das condicoes seja satisfeita
else:
    if( (gcoe>=-2 and gcoe<=0) and (gcod>=-2 and gcod<=0)): # Analisa as condicoes para o uso da lente prime
        if(geoe<=-3 and geoe>=-10) and (geod<=-3 and geod>=-10):
            print("Recomenda-se a lente prime")
            flag = 1
    if((gcoe>=-5 and gcoe<=0) and (gcod>=-5 and gcod<=0) and flag!=1): # Analisa as condicoes para o uso da lente vision
        if(geoe<=0 and geoe>=-15) and (geod<=-0 and geod>=-15):
            print("Recomenda-se a lente vision")
            flag = 2
    if(flag != 1 and flag !=2): print("Nao ha nenhuma lente disponivel no momento") # Caso nenhuma das condicoes seja satisfeita