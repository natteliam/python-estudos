#Primeiramente coletamos os dados do pet (cão).
nome_pet = input("Digite o nome do pet: ").strip().title()
peso_pet = float(input("Digite o peso do pet: ").replace(",", "."))
castrado = input("Castração (sim/não): ").lower()
obesidade = input("Está com obesidade (sim/não)? ").lower()
nivel_atividade = input("Digite o nível de atividade (baixo/médio/alto): ").lower()

#Montamos a função para calcular as kcal, a depender do nível de atividade, do peso e da castração.
#Fator obesidade reduz drasticamente o fator de multiplicação.
def calcular_kcal(peso_pet):
    if obesidade == "sim":
        kcal = 70 * (peso_pet ** 0.75)

    elif castrado == "sim" and nivel_atividade == "baixo":
        kcal = 95 * (peso_pet ** 0.75)

    elif castrado == "não" and nivel_atividade == "baixo":
        kcal = 95 * (peso_pet ** 0.75)

    elif castrado == "sim" and nivel_atividade == "médio":
        kcal = 100 * (peso_pet ** 0.75)

    elif castrado == "não" and nivel_atividade == "médio":
        kcal = 110 * (peso_pet ** 0.75)

    elif castrado == "sim" and nivel_atividade == "alto":
        kcal = 110 * (peso_pet ** 0.75)

    elif castrado == "não" and nivel_atividade == "alto":
        kcal = 120 * (peso_pet ** 0.75)

    return kcal

#Vamos converter a variável calorias a partir da função criada acima.
calorias = calcular_kcal(peso_pet)

#Imprime o resultado.
print(f"Considerando que o nível de atividade física é {nivel_atividade} e que você respondeu {castrado} para o fator castração, o pet {nome_pet} precisa ingerir em média {calorias:.2f} kcal por dia.")
