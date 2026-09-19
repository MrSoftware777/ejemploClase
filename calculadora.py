def calculadora():
    print("--- CALCULADORA BÁSICA ---")
    try:
        num1 = float(input("Ingrese el primer número: "))
        operacion = input("Operación (+, -, *, /): ").strip()
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    calculadora()