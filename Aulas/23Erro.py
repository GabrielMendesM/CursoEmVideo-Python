try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError) as erro:
    print(f"ERRO foi: {erro}")
except Exception as erro:
    print(f"ERRO foi {erro.__class__}")
else:
    print(f"O resultado de {a}/{b} foi {r}")
finally:
    print("Vai acontecer independente.")