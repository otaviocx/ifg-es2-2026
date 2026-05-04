def is_primo(numero):
    if type(numero) == str and len(numero) == 0:
        return False
    try:
      numero = int(numero)
    except ValueError:
        return False
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
if __name__ == "__main__":
    num = int(input("Digite um número: "))
    if is_primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
