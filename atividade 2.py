import random
import statistics
import collections


class Entradas():
    def __init__(self, valor, pesos):
        self.valor = int(valor)
        self.pesos = dict(pesos)


def somatorio(entradas, peso):
    print(f'Peso do Somatório selecionado = {peso}')
    print('')
    constante = 0
    valor_somatorio = 0
    for e in entradas:
        valor_somatorio += e['valor'] * e['pesos'][peso]
    return round(valor_somatorio + constante, 2)


def media(entradas, peso):
    arranjo_media = []
    for e in entradas:
        n_peso = e['pesos'][peso]
        arranjo_media.append(float(n_peso))
    return statistics.mean(arranjo_media)


def mediana(entradas, peso):
    arranjo_media = []
    for e in entradas:
        n_peso = e['pesos'][peso]
        arranjo_media.append(float(n_peso))
    return statistics.median(arranjo_media)


def moda(entradas, peso):
    arranjo_media = []
    for e in entradas:
        n_peso = e['pesos'][peso]
        arranjo_media.append(float(n_peso))
    return statistics.mode(arranjo_media)


def media_harmonica(entradas, peso):
    arranjo_media = []
    for e in entradas:
        n_peso = e['pesos'][peso]
        arranjo_media.append(float(n_peso))
    return statistics.harmonic_mean(arranjo_media)


def ocorrencia(entradas, peso):
    arranjo_media = []
    for e in entradas:
        n_peso = e['pesos'][peso]
        arranjo_media.append(float(n_peso))
    return collections.Counter(arranjo_media)


def custo(valor_obitido, valor_ideal):
    return round(((valor_obitido - valor_ideal) ** 2), 2)


def gerar_pesos(qtd_pesos):
    pesos = {}
    for n_peso in range(qtd_pesos):
        pesos[f'w{n_peso}'] = round(random.random(), 2)
    return pesos


def gera_lista_entradas(qtd_entradas, qtd_pesos_por_entradas):
    entradas = []
    for n_entradas in range(qtd_entradas):
        vars()[f'e{str(n_entradas)}'] = {
            "nome": f'Entrada {str(n_entradas)}',
            "valor": round(random.random(), 2),
            "pesos": gerar_pesos(qtd_pesos_por_entradas)
        }
        entradas.append(vars()[f'e{str(n_entradas)}'])
    return entradas


def chamada_peso_randomico(entrada):
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'


def chamada_peso_randomico(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'


def print_lista_entradas(entradas):
    for item in entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')


def print_lista_entradas_bruta(entradas):
    for item in entradas:
        print(item)
    print("\n")


def run():
    # variaveis de entradas e pesos
    qtd_entradas = 10
    qtd_pesos = 10

    print('\n=-=-=-=-=-=-=-= Start =-=-=-=-=-=-=-=\n')
    print(f'Quantidade de entradas: {qtd_entradas}\nQuantidade de pesos por entrada: {qtd_pesos}\n')

    entradas = gera_lista_entradas(qtd_entradas, qtd_pesos)

    print_lista_entradas(entradas)

    somatorios = somatorio(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Função de Ativação: {somatorios}')

    custos = custo(somatorios, 1)

    print(f'Valor da Função de Custo: {custos}')

    medias = media(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Média: {medias}')

    medianas = mediana(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Mediana: {medianas}')

    modas = moda(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Moda: {modas}')

    media_harmonicas = media_harmonica(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'Valor da Harmônica: {media_harmonicas}')

    ocorrencias = ocorrencia(entradas, chamada_peso_randomico(qtd_pesos))

    print(f'{ocorrencias}')

    print('\n=-=-=-=-=-=-=-=- End -=-=-=-=-=-=-=-=\n')


if __name__ == '__main__':
    run()

