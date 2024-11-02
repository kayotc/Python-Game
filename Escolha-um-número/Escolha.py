import random




aleatorio = random.randint(1, 100) # Escolhe o número de 1 a 100



print("O computador escolheu um número alétorio")
print("                       ")
print("-=-=-=-=-=-" * 5)
print("-=-=-=-=-=-" * 5)
print("                       ")

num_tentativas = -1

while True: 
    try:
        num_tentativas +=1
        print("Esse é seu número de tentativas: " , num_tentativas )
        print("                       ")
    
        
        tentativa = float(input("Adivinhe qual número ele escolheu: ")) 
        print("                       ")

        if tentativa == aleatorio:
            print("                       ")
            print(f"É esse o número {aleatorio}. Parabéns, você acertou!!")
            print("                       ")
            print(f"Você acertou em {num_tentativas} tentivas")
            break 

        if num_tentativas > 9:
            print(f"Você tentou {num_tentativas} vezes, você perdeu")
            print("                       ")
            print(f"O número que a máquina escolheu foi {aleatorio}")
            break

        elif tentativa < aleatorio:
            print("                       ")
            print("O número é maior")
            

        elif tentativa > aleatorio:
            print("                       ")
            print("O número é menor")
        
    
 
    except ValueError:
        print("                       ")
        print("Apenas números")
    

           















