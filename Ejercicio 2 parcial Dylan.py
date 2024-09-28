def calcular_superficie(base, altura):
    return base * altura

# Bloque principal
def main():
    # Cargar lados del primer rectángulo
    base1 = float(input("Ingrese la base del primer rectángulo: "))
    altura1 = float(input("Ingrese la altura del primer rectángulo: "))
    
    # Cargar lados del segundo rectángulo
    base2 = float(input("Ingrese la base del segundo rectángulo: "))
    altura2 = float(input("Ingrese la altura del segundo rectángulo: "))
    
    # Calcular superficies
    superficie1 = calcular_superficie(base1, altura1)
    superficie2 = calcular_superficie(base2, altura2)
    
    # Mostrar resultados
    print(f"Superficie del primer rectángulo: {superficie1}")
    print(f"Superficie del segundo rectángulo: {superficie2}")

    if superficie1 > superficie2:
        print("El primer rectángulo tiene una superficie mayor.")
    elif superficie2 > superficie1:
        print("El segundo rectángulo tiene una superficie mayor.")
    else:
        print("Ambos rectángulos tienen la misma superficie.")

if __name__ == "__main__":
    main()
