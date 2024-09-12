# 2. Escreva um programa que leia uma lista de números inteiros e exiba-os em ordem crescente

def main() -> None:
    listNumbers: str = input("Please enter the list of numbers you want in ascending order, separated by spaces: ")
    listNumbers = listNumbers.split()
    result = [int(num) for num in listNumbers]
    result.sort()
        
    print(f"The list of numbers in ascending order is: {result}")
    
if __name__ == "__main__":
    main()
