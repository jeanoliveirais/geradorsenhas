# password_generator.py
import random
import string

def generate_password(length=12):
    """Gera uma senha aleatória com o comprimento especificado."""
    if length < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    try:
        length = int(input("Digite o comprimento da senha (mínimo 8): "))
        password = generate_password(length)
        if password:
            print(f"Sua senha gerada é: {password}")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
