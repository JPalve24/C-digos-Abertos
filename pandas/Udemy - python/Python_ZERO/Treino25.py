# Recursividade

def fatorial(num):
    if num == 1:
        return 1

    return num * fatorial(num - 1)

fator = fatorial(int(input("Digite um número para descobrir o fatorial: ")))

print(f"O fatorial é: {fator}")