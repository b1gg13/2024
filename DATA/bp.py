# b_pit (bottomless pit) is a program that inputs type of food from a specific
# list bad prints ot a messege according to what is accorded to the variable...
def b_pit( s1, g2, b3, n4, f5, n6):
    if si:
        print('si nimeshiba')
    elif g2:
        print('leo pia me niitwe mluhya')
    elif b3:
        print('sina ngori')
    elif n4:
        print ('leo nayo umelala njaa')
    elif f5:
        print ('budo uliwai ketchup ngapi kwani')
    elif n6:
        print('sina beef')
    else:
        print('si lazima pia udishi')

menu = [
    ['sembe-(s1)', 'gweno-(g2)', 'beef-(b3)'],
    ['noodles-(n4)', 'frys-(f5)', 'ngori-(n6)']
]
#print out entire list for user ind asks
print(menu[0][0])
print(menu[0][1])
print(menu[0][2])
print(menu[1][0])
print(menu[1][1])
print(menu[1][2])
print('\n')


b_pit = input("hungry? enter item code:")
