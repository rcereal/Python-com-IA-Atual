# FUNÇÕES

# TODA FUNÇÃO IRA RETORNAR ALGO POR MAIS QUE NAO DEFINA O RETORNO
# def nome_funcao(parametros)
#     return codigo

# def soma(primeiro_numero, segundo_numero):
#     '''
#     Função para somar dois valores
#     '''
#     return primeiro_numero + segundo_numero

# soma(2,5)
def contador_letras(lista):
    nova_lista_com_cores_que_possui_mais_de_quatro_letras = []

    for cor in lista:
        # percorrer a lista e verificar qual valor tem mais de quatro contador_letras
        # se o valor tiver mais de quatro letras adicionar mais de quatro contador_letras
        # adicionara na nova lista
        if len(cor) > 4:
            nova_lista_com_cores_que_possui_mais_de_quatro_letras.append(cor)
    return nova_lista_com_cores_que_possui_mais_de_quatro_letras