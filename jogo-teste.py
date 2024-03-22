print("Vamos jogar um jogo! \n")
nome=str(input("Digite seu nome: "))
print("\n")
print(f"Seja bem vindo {nome}! \n")
idade=(f"Quantos anos você tem? ")
pontuacao=0
questao1=int(input("Qual é o resultado da operação: 47*3? "))
if questao1==141:
    print("Você acertou! Próxima questão. \n")
    pontuacao+=1
else:
    print("Você errou, próxima questão. \n")
print(f"Sua pontuação atual é {pontuacao} \n")
questao2=float(input("Você tem 2 maçãs e divide para 4 amigos e você não comeu: Quantas maçãs cada amigo comeu? Escreva em número decimal: "))
if questao2==0.50:
    print("Você acertou! Próxima questão. \n")
    pontuacao+=1
else:
    print("Você errou, próxima questão. \n")
print(f"Sua pontuação atual é {pontuacao}. \n")
questao3=str(input("A américa é um...? "))
if questao3=="continente" or questao3=="Continente":
    print("Você acertou! Próxima questão.\n")
    pontuacao+=1
elif questao3=="país" or questao3=="País":
    print(f"POR ACASO VOCÊ É UM IDIOTA?????????? PELO AMOR DE DEUS {nome} VAI ESTUDAR, REPROVADO")
    exit()
else:
    print("Você errou, próxima questão. \n")
print(f"Sua pontuação atual é {pontuacao} \n")
print("Escreva a soma do número das alternativas corretas: As cores da bandeira do Brasil são: ")
print("   1: Verde      2: Vermelho \n 4: Amarelo      8: Azul \n 16: Branco      32:Preto")
questao4=int(input("Digite a soma das alternativas corretas: "))
if questao4==29:
    print("Você acertou! Próxima questão. \n")
    pontuacao+=1
else:
    print("Você errou, próxima questão. \n")
print(f"Sua pontuação atual é {pontuacao}\n")
print("Escolha a alternativa correta: \n")
questao5=str(input("O sol nasce na direção: \n a) Sul      b) Leste\n c) Oeste    d) Norte \n"))
if questao5=="b" or questao5=="B":
    print("Você acertou! Pŕoxima questão.\n")
    pontuacao+=1
else:
    print("Você errou, próxima questão \n")
print(f"Sua pontuação atual é {pontuacao}. \n")
if pontuacao==0:
    print("Você é muito burro mano, perdeu muito cedo, boa noite.\n")
    exit()
questao6=int(input("Adivinha o número que estou pensando (1-100): \n"))
if questao6==47:
   print("Você acertou! Próxima questão.\n")
   pontuacao+=1
elif questao6<47 and questao6>40 or questao6>47 and questao6<54:
    questao6=int(input("Muito perto, tente denovo: \n"))
    if questao6==47:
        print("Você acertou! Pŕoxima questão.\n")
        pontuacao+=1
else:
    print("Você errou, próxima questão. \n")
print(f"Sua pontuação atual é {pontuacao}.\n")
questao7=str(input("Qual é o planeta mais quente do sistema solar? "))
if questao7=="Vênus" or questao7=="vênus" or questao7=="venus" or questao7=="Venus":
    print("Você acertou! Próxima questão. \n")
    pontuacao+=1
elif questao7=="Mercurio" or questao7=="Mercúrio" or questao7=="mercúrio" or questao7=="mercurio":
    print("Por pouco mano, mas você errou, próxima questão.\n")
else:
    print("Você errou, próxima questão.\n")
print(f"Sua pontuação atual é {pontuacao}")
questao8=str(input("Plutão é um planeta? "))
if questao8=="não" or questao8=="Não" or questao8=="nao" or questao8=="Nao":
    print("Você acertou! Próxima questão.\n")
    pontuacao+=1
else:
    print("Você errou, próxima questão.\n")
print(f"Sua pontuação atual é {pontuacao}\n")
questaox=str(input("Digite a sigla do estado onde você mora: "))
if questaox=="RS" or questaox=="RJ" or questaox=="SP":
    print("Reprovado.")
    exit()
else:
    print("Beleza. Só por curiosidade. \n")
questao9=str(input("Qual dessas marcas vendem processadores de computadores?\n a) Dell     b) Fiat\n c) Intel    d) Brastemp"))
if questao9=="c" or questao9=="C":
    print("Você acertou! Próxima questão.\n")
    pontuacao+=1
else:
    print("Você errou, próxima questão.\n")
print(f"Sua pontuação atual é {pontuacao}\n")

