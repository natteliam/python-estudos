#Primeiramente, coletamos os dados que vamos precisar.
nome_pet = input("Digite o nome do pet: ")
especie = input("Digite a espécie do pet: ")
responsavel = input("Digite o seu nome completo: ")

#Função para formatar o nome do pet.
def formatar_pet(nome_pet):
    nome_formatado = nome_pet.strip().title()
    return nome_formatado

#Função para formatar a espécie do pet.
def formatar_especie(especie):
    especie_formatado = especie.strip().lower()
    if especie_formatado == "cão" or especie_formatado == "cao":
        return "Espécie canina."
    elif especie_formatado == "gato":
        return "Espécie felina."
    else:
        return "Espécie não cadastrada."

#Função para formatar o nome do responsável.
def formatar_responsavel(responsavel):
    responsavel_formatado = responsavel.strip().title()
    return responsavel_formatado

#Função para criar a ficha final. Essa função chama as outras funções.
def criar_ficha(nome_pet, especie, responsavel):
    nome_pet_formatado = formatar_pet(nome_pet)
    especie_formatada = formatar_especie(especie)
    responsavel_formatado = formatar_responsavel(responsavel)
    return f"Paciente: {nome_pet_formatado} | {especie_formatada} | Responsável: {responsavel_formatado}"

#Por fim, imprime a ficha.
ficha = criar_ficha(nome_pet, especie, responsavel)
print(ficha)
