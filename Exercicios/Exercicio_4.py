# 4. Escreva um programa que valide senhas com base nos critérios: tenha pelo menos 8 caracteres,
# contendo letras maiúsculas, minúsculas, números e caracteres especiais

def main() -> None:
    password = input("Digite a senha: ")
    if len(password) < 8:
        print("Senha muito curta")
        return
    if not any(char.isupper() for char in password):
        print("Senha não contém letras maiúsculas")
        return
    if not any(char.islower() for char in password):
        print("Senha não contém letras minúsculas")
        return
    if not any(char.isdigit() for char in password):
        print("Senha não contém números")
        return
    if not any(not char.isalnum() for char in password):
        print("Senha não contém caracteres especiais")
        return
    else:
        print("Senha válida")

if __name__ == "__main__":
    main()