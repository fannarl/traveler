# Skrifið Python forrit sem les inn eina jákvæða heiltölu, n, frá notanda og skrifar síðan út aðra hverja heiltölu frá n niður í 1, 
# eina í hverri línu. Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.

n = int(input('Input a integer: '))

for i  in range(n, 1, -2):
    print(i)

# n = int(input("Input an integer: "))

# i = 1
# while n >= i:
#     print(n)
#     n -= 2