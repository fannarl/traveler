def readNumbers():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    return numbers


def sumOfEvens(numbers):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return sum(evens)

def main():
    numbers = readNumbers()
    print("Sum of even numbers:" , sumOfEvens(numbers))

main()