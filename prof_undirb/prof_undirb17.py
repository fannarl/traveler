# Skrifið Python forrit sem les inn lista L af pósitívum heiltölum (e. integers) og prentar út eftirfarandi upplýsingar:
# Listann L.
# Raðaða útgáfu af L.
# Raðaðan lista af einkvæmum (e. unique) prímtölum í L. 
# Min, max og meðaltal gilda í L.  Meðaltalið skal skrifa út með tveimur aukastöfum.
# Þið megið nota listaföll í útfærslunni en þið megið ekki nota neina import setningu.   Fallið is_prime() er gefið.
# Prenta þarf út villuskilaboð ef notandinn slær ekki eingöngu heiltölur inn í listann.  Sjá dæmi um inntak/úttak fyrir neðan.

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def get_prime_list(arr):
    result = []
    for i in arr:
        if is_prime(i):
            result.append(i)
    return list(set(result))

numbers = input('Input a comma seperated list: ')
str_arr = numbers.split(',')
try:
    int_arr = [int(i) for i in str_arr]
    print('Input list: ', end='')
    print(int_arr)
    print('Sorted list: ', end='')
    print(sorted(int_arr))
    print('Prime list: ', end='')
    print(sorted(get_prime_list(int_arr)))
    print('Min: {0}, Max: {1}, Average: {2:.2f}'.format(min(int_arr), max(int_arr), sum(int_arr)))
except ValueError:
    print('Incorrect input!')
except:
    print("Something strange happened, FLY YOU FOOLS!")

