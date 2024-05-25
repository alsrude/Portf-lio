pessoa = {
    'FICHA:': 'Pessoa selecionada',
    'Nome': 'Mirela',
    'Sobrenome': 'Emilio',
}

dados_pessoa = {
    'Idade': 18,
    'Altura': 1.60,
}

dados = {**pessoa, **dados_pessoa}

def argumentos_nomeados(*args, **kwargs):
    
    for chave, valor in kwargs.items():
        print(chave, valor)


argumentos_nomeados(**dados)
    
