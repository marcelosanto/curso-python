# for/else
lista = ['Oracle', 'Java', 'SqlServer',
         'Delphi', 'Python', 'Android', 'Oracle']

comeca_com_o = False

for list in lista:
    if list.lower().startswith('o'):
        comeca_com_o = True

if comeca_com_o:
    print('Existe uma palavra que comeca com O')
else:
    print('Não existe uma palavra que comeca com O')
