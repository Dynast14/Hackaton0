def evaluate_expression(expression):
    try:
        # Filtrar la expresión para permitir solo caracteres válidos
        allowed_operators = "+-*/()"
        filtered_expression = ''.join(c for c in expression if c in allowed_operators or c.isdigit() or c.isspace())
        # Evaluar la expresión
        result = eval(filtered_expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Calculadora en línea de comandos")
    print("Escribe la operación (por ejemplo, 2 + (2 + 2)) y presiona Enter")
    print("Presiona 'c' para borrar la operación")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.strip().lower() == 'c':
                continue
            
            result = evaluate_expression(user_input)
            print(result)
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
