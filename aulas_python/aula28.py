"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0                                       
contrário disso:                                        
    resultado é o valor da conta                     

O primeiro dígito do CPF é 7
"""
import os, re, sys

entrada = input('CPF[122.338.849-22]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
entrada 
)
entrada_e_sequencial = entrada == entrada [0]*len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

  
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
dez_digitos = cpf_enviado_usuario[:10]
contador_regressivo_2 = 11

resultado_digito_2 = 0
resultado_digito_1 = 0 
print(f'CPF: {cpf_enviado_usuario}')

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1 
digito_1 = (resultado_digito_1*10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 


for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1 
digito_2 = (resultado_digito_2*10) %11
digito_2 = digito_2 if digito_2 <= 9 else 0 
      

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    os.system ('cls')
    print(f'Seu CPF: {cpf_enviado_usuario} é válido!')
else:
    os.system ('cls')
    print(f'Seu CPF: {cpf_enviado_usuario} é INVÁLIDO!')


