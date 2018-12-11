# Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(key):
    if key in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

key = int(input('Check if key excists: '))
is_key_present(key)