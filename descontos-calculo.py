n1 = float(input('Qual o preço de um produto? R$'))
n2 = float(input('Qual a porcentagem da promoção? '))
n3 = n1 - n1*(n2/100)
 

print(f'O produto que custava R${n1}, com {n2}% passará a custar R${n3}')