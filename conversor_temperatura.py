temp_c = input('Digite uma temperatura em ºC: ').replace(',','.')

temp_k = round(273.15 + float(temp_c), 2)

print('Temperatura em Kelvin {:.2f}'.format(temp_k).replace('.',','))