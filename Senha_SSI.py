import re

# Definição das regras
min_length = 12
min_uppercase = 1
min_lowercase = 1
min_digits = 1
min_special_chars = 1

# Função para validar a senha
def validate_password(password):
    # Verifica o comprimento mínimo
    if len(password) < min_length:
        return False, f"A senha deve ter pelo menos {min_length} caracteres."

    # Verifica a presença de letras maiúsculas, minúsculas, números e caracteres especiais
    if not re.search(r"[A-Z]", password):
        return False, f"A senha deve conter pelo menos {min_uppercase} letra(s) maiúscula(s)."
    if not re.search(r"[a-z]", password):
        return False, f"A senha deve conter pelo menos {min_lowercase} letra(s) minúscula(s)."
    if not re.search(r"\d", password):
        return False, f"A senha deve conter pelo menos {min_digits} número(s)."
    if not re.search(r"[!@#$%^&*]", password):
        return False, f"A senha deve conter pelo menos {min_special_chars} caractere(s) especial(is)."

    # Verifica se a senha é uma palavra comum
    common_passwords = ["senha", "123456", "qwerty", "123456789", "admin"]
    if password.lower() in common_passwords:
        return False, "A senha escolhida é muito comum. Escolha uma senha mais segura."

    # Se todas as regras foram cumpridas, retorna True
    return True, "Senha válida."

# Exemplo de uso
password = input("Digite uma senha: ")
is_valid, message = validate_password(password)
if is_valid:
    print("Senha criada com sucesso!")
else:
    print(f"Erro: {message}")
