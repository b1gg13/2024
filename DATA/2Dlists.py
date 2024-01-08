
ranD =  [
    ['joe', 3 , 'ike'],
    ['dee','dan', 69],
    [7 , 'sam', 678 ]
]
#prints out specified items on the list...
print("specipic items \n")
print(ranD[1][1])
print(ranD[0][1])
print(ranD[1][0])
print(ranD[0][0])

#prints out entire list...
print ("\n entire list")
for row in ranD:
    for col in row:
        print(col)
