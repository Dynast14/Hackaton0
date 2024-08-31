def add(x, y):
    return x + y

def divide(x, y):
    if b != 0:
        return x / y
    else:
        return "Error:  División por      cero"
def subtract(a, b):
    return a - b

def main():
    print("Calculadora en línea de comandos")
    print("Escribe la operación (por ejemplo, 2 + 2) y presiona Enter")
    print("Presiona 'c' para borrar la operación")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.strip().lower() == 'c':
                continue
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Operación inválida. Usa el formato 'a operador b'")
                continue
            
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
            
            if operator == '-':
                print(subtract(a, b))
            else:
                print("Operador no reconocido. Usa '+', '-', '*' o '/'")
        except ValueError:
            print("Entrada inválida. Asegúrate de usar números y operadores válidos.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
