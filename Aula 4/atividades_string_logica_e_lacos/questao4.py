senha = input("Digite a senha : ")

def checar_senha(senha):
    if len(senha) >= 8 and any(char.islower() for char in senha) and any(char.isupper() for char in senha) and any(char.isdigit() for char in senha):
        print("Senha forte")
    else:
        print("Senha fraca")

checar_senha(senha)