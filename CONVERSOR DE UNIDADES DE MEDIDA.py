valor = eval(input('Insira um valor qualquer: '))
print('1.km')
print('2.hm')
print('3.dam')
print('4.m')
print('5.dm')
print('6.cm')
print('7.mm')
unidade = int(input('Qual é a sua unidade de medição? '))
if unidade == 1:
    print('1.hm')
    print('2.dam')
    print('3.m')
    print('4.dm')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} km para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} km equivalem a {} hm'.format(valor,valor * (10 ** 1)))
    elif unidade2 == 2:
        print('{} km equivalem a {} dam'.format(valor, valor * (10 ** 2)))
    elif unidade2 == 3:
        print('{} km equivalem a {} m'.format(valor, valor * (10 ** 3)))
    elif unidade2 == 4:
        print('{} km equivalem a {} dm'.format(valor, valor * (10 ** 4)))
    elif unidade2 == 5:
        print('{} km equivalem a {} cm'.format(valor, valor * (10 ** 5)))
    elif unidade2 == 6:
        print('{} km equivalem a {} mm'.format(valor, valor * (10 ** 6)))
if unidade == 2:
    print('1.km')
    print('2.dam')
    print('3.m')
    print('4.dm')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} hm para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} hm equivalem a {} km'.format(valor,valor / (10 ** 1)))
    elif unidade2 == 2:
        print('{} hm equivalem a {} dam'.format(valor, valor * (10 ** 1)))
    elif unidade2 == 3:
        print('{} hm equivalem a {} m'.format(valor, valor * (10 ** 2)))
    elif unidade2 == 4:
        print('{} hm equivalem a {} dm'.format(valor, valor * (10 ** 3)))
    elif unidade2 == 5:
        print('{} hm equivalem a {} cm'.format(valor, valor * (10 ** 4)))
    elif unidade2 == 6:
        print('{} hm equivalem a {} mm'.format(valor, valor * (10 ** 5)))
if unidade == 3:
    print('1.km')
    print('2.hm')
    print('3.m')
    print('4.dm')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} dam que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} dam equivalem a {} km'.format(valor,valor / (10 ** 2)))
    elif unidade2 == 2:
        print('{} dam equivalem a {} hm'.format(valor, valor / (10 ** 1)))
    elif unidade2 == 3:
        print('{} dam equivalem a {} m'.format(valor, valor * (10 ** 1)))
    elif unidade2 == 4:
        print('{} dam equivalem a {} dm'.format(valor, valor * (10 ** 2)))
    elif unidade2 == 5:
        print('{} dam equivalem a {} cm'.format(valor, valor * (10 ** 3)))
    elif unidade2 == 6:
        print('{} dam equivalem a {} mm'.format(valor, valor * (10 ** 4)))
if unidade == 4:
    print('1.km')
    print('2.hm')
    print('3.dam')
    print('4.dm')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} m para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} m equivalem a {} km'.format(valor, valor / (10 ** 3)))
    elif unidade2 == 2:
        print('{} m equivalem a {} hm'.format(valor, valor / (10 ** 2)))
    elif unidade2 == 3:
        print('{} m equivalem a {} dam'.format(valor, valor / (10 ** 1)))
    elif unidade2 == 4:
        print('{} m equivalem a {} dm'.format(valor, valor * (10 ** 1)))
    elif unidade2 == 5:
        print('{} m equivalem a {} cm'.format(valor, valor * (10 ** 2)))
    elif unidade2 == 6:
        print('{} m equivalem a {} mm'.format(valor, valor * (10 ** 3)))
if unidade == 5:
    print('1.km')
    print('2.hm')
    print('3.dam')
    print('4.m')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} dm para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} dm equivalem a {} km'.format(valor, valor / (10 ** 4)))
    elif unidade2 == 2:
        print('{} dm equivalem a {} hm'.format(valor, valor / (10 ** 3)))
    elif unidade2 == 3:
        print('{} dm equivalem a {} dam'.format(valor, valor / (10 ** 2)))
    elif unidade2 == 4:
        print('{} dm equivalem a {} m'.format(valor, valor / (10 ** 1)))
    elif unidade2 == 5:
        print('{} dm equivalem a {} cm'.format(valor, valor * (10 ** 1)))
    elif unidade2 == 6:
        print('{} dm equivalem a {} mm'.format(valor, valor * (10 ** 2)))
if unidade == 6:
    print('1.km')
    print('2.hm')
    print('3.dam')
    print('4.m')
    print('5.cm')
    print('6.mm')
    unidade2 = int(input('Deseja converter {} cm para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} cm equivalem a {} km'.format(valor, valor / (10 ** 5)))
    elif unidade2 == 2:
        print('{} cm equivalem a {} hm'.format(valor, valor / (10 ** 4)))
    elif unidade2 == 3:
        print('{} cm equivalem a {} dam'.format(valor, valor / (10 ** 3)))
    elif unidade2 == 4:
        print('{} cm equivalem a {} m'.format(valor, valor / (10 ** 2)))
    elif unidade2 == 5:
        print('{} cm equivalem a {} dm'.format(valor, valor / (10 ** 1)))
    elif unidade2 == 6:
        print('{} cm equivalem a {} mm'.format(valor, valor * (10 ** 1)))
if unidade == 7:
    print('1.km')
    print('2.hm')
    print('3.dam')
    print('4.m')
    print('5.dm')
    print('6.cm')
    unidade2 = int(input('Deseja converter {} mm para que outra unidade acima? '.format(valor)))
    if unidade2 == 1:
        print('{} mm equivalem a {} km'.format(valor, valor / (10 ** 6)))
    elif unidade2 == 2:
        print('{} mm equivalem a {} hm'.format(valor, valor / (10 ** 5)))
    elif unidade2 == 3:
        print('{} mm equivalem a {} dam'.format(valor, valor / (10 ** 4)))
    elif unidade2 == 4:
        print('{} mm equivalem a {} m'.format(valor, valor / (10 ** 3)))
    elif unidade2 == 5:
        print('{} mm equivalem a {} dm'.format(valor, valor / (10 ** 2)))
    elif unidade2 == 6:
        print('{} mm equivalem a {} cm'.format(valor, valor / (10 ** 1)))
print('Obrigado!')