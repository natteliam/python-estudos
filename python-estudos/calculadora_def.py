def calculadora_kcal(peso, castrado, atividade, obesidade):
    if obesidade == "sim":
        kcal = 70 * (peso ** 0.75)

    elif castrado == "sim" and atividade == "baixo":
        kcal = 90 * (peso ** 0.75)

    elif castrado == "não" and atividade == "baixo":
        kcal = 95 * (peso ** 0.75)

    elif castrado == "sim" and atividade == "médio":
        kcal = 95 * (peso ** 0.75)

    elif castrado == "não" and atividade == "médio":
        kcal = 100 * (peso ** 0.75)

    elif castrado == "sim" and atividade == "alto":
        kcal = 100 * (peso ** 0.75)

    elif castrado == "não" and atividade == "alto":
        kcal = 110 * (peso ** 0.75)

    elif castrado == "sim" and atividade == "muito alto":
        kcal = 110 * (peso ** 0.75)

    elif castrado == "não" and atividade == "muito alto":
        kcal = 120 * (peso ** 0.75)

    return kcal

def sim_ou_nao(pergunta):
    while pergunta not in ["sim", "não"]:
        print(
            f"\n"
            f"Resposta inválida, responda com sim ou não."
        )
        pergunta = input("Lembre-se da acentuação! Digite novamente: \n").lower().strip()

    return pergunta

def validar_atividade(resposta):
    while resposta not in ["baixo", "médio", "alto", "muito alto"]:
        print(
            f"\n"
            f"Resposta inválida, responda com baixo, médio, alto ou muito alto.\n"
        )
        resposta = input("Lembre-se da acentuação! Digite novamente: \n").lower().strip()

    return resposta

def main():
    nome_pet = input("Digite o nome do pet: ").strip().title()
    peso = float(input("Digite o peso do pet: ").replace(",","."))
    castrado = input("Castração (sim/não): ").lower().strip()
    castrado = sim_ou_nao(castrado)
    atividade = input("Nível diário de atividade (baixo/médio/alto/muito alto): ").lower().strip()
    atividade = validar_atividade(atividade)
    obesidade = input("Tem obesidade (sim/não): ").lower().strip()
    obesidade = sim_ou_nao(obesidade)

    kcal = calculadora_kcal(
        peso,
        castrado,
        atividade,
        obesidade
    )

    print(
    f"\n"
    f"----- RESULTADO -----\n"
    f"\n"
    f"Paciente: {nome_pet}\n"
    f"Peso atual: {peso:.2f} kg\n"
    f"Castrado: {castrado}\n"
    f"Nível de atividade: {atividade}\n"
    f"\n"
    f"Necessidade energética:\n"
    f"{kcal:.2f} kcal por dia.\n"
    )

if __name__ == "__main__":
    main()
