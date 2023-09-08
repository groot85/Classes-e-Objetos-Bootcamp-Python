# 1. Crie uma classe que modele o objeto "carro".
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# 3. Um carro tem os seguintes comportamentos (metodo - acao - funcoes especificas de uma classe): liga, desliga, acelera, desacelera.

#self significa eu mesmo

class Carro: #ao criar uma classe estamos criando um "padrao" para chamar o objeto em outros momentos, com "adjetivos" que o personalizar
    def __init__ (self, cor, modelo): #metodo construtor def __init__ (self (é o carro) , os atributos listados separados por virgula. No nosso caso, carro parte sempre desligado e velocidade 0. Entao, nao precisa colocar esses dadaos. )
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0.0
        self.lim_vel = 180.0

    def liga (self):
        self.ligado = True
  
    def desliga (self):
        self.ligado = False
        self.velocidade = 0.0
  
    def acelera (self):
        if self.ligado == False:
            return
  
        if self.velocidade < self.lim_vel:
            self.velocidade += 5
  
    def desacelera (self):
        if self.ligado == False:
            return
        
        if self.velocidade > 0:
            self.velocidade -= 5
  
    def __str__ (self):
        ligado_str = "ligado" if self.ligado == True else "desligado"
        return f"Carro {self.modelo} da cor {self.cor} está {ligado_str}, à velocidade de {self.velocidade} km/h"

# 4. Crie uma instância da classe carro.
carro = Carro ("amarelo", "Fiat Stilo")
print (carro)  

# 5. Faça o carro "andar" utilizando os métodos da sua classe.
carro.liga() #ligando o carro para depois comecar a acelerar
print(carro)

for i in range (7): #quantas vezes quero que o carro acelere
    carro.acelera() #definido lá no início o valor do acelerador
print(carro)

# 6. Faça o carro "parar" utilizando os métodos da sua classe.
for i in range (6): #quantas vezes quero que o carro desacelere
    carro.desacelera() #definido lá no início o valor do desacelerador
print(carro)

#depois de desacelerar, carro desliga :) 
carro.desliga()
print (carro)

