nome_pet = input("Digite o nome do pet: ")
especie = input("Digite a espécie do pet: ")
responsavel = input("Digite o seu nome completo: ")

def formatar_pet(nome_pet):
    nome_formatado = nome_pet.strip().title()
    return nome_formatado

def formatar_especie(especie):
    especie_formatado = especie.strip().lower()
    if especie_formatado == "cão" or especie_formatado == "cao":
        return "Espécie canina."
    elif especie_formatado == "gato":
        return "Espécie felina."
    else:
        return "Espécie não cadastrada."

def formatar_responsavel(responsavel):
    responsavel_formatado = responsavel.strip().title()
    return responsavel_formatado

def criar_ficha(nome_pet, especie, responsavel):
    nome_pet_formatado = formatar_pet(nome_pet)
    especie_formatada = formatar_especie(especie)
    responsavel_formatado = formatar_responsavel(responsavel)
    return f"Paciente: {nome_pet_formatado} | {especie_formatada} | Responsável: {responsavel_formatado}"

ficha = criar_ficha(nome_pet, especie, responsavel)
print(ficha)
