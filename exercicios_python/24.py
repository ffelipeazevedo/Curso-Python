from datetime import date

while True:
    ano_atual = date.today().year
    ano_nascimento = input('Digite o ano de nascimento: ')


    if not ano_nascimento.isdigit() or len(ano_nascimento) != 4:
        print('Por favor digite um ano de nascimento válido (com 4 digítos)!')
        continue

    ano_nascimento = int(ano_nascimento)
    idade = ano_atual - ano_nascimento
    prazo = idade - 18
    qt_tempo_falta = 18 - idade
    

    if idade == 18:
        print(f'Você tem: {idade} anos, e deverá se alistar!')
    elif idade > 18:
        print(f'Você tem: {idade} anos, e passou {prazo} anos do prazo de se alistar!')
    elif idade < 18:
        print(f'Você tem: {idade} anos, e ainda falta {qt_tempo_falta} anos para se alistar!')
    break
