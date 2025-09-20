class AFN:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
    
    def procesar_cadena(self, cadena):
        """Procesa una cadena usando el AFN (análisis por hilos)"""
        estados_actuales = {self.estado_inicial}
        
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False
            
            nuevos_estados = set()
            for estado in estados_actuales:
                transicion = (estado, simbolo)
                if transicion in self.transiciones:
                    nuevos_estados.update(self.transiciones[transicion])
            
            estados_actuales = nuevos_estados
            if not estados_actuales:
                return False
        
        # Verificar si al menos un estado final es de aceptación
        return any(estado in self.estados_aceptacion for estado in estados_actuales)

def crear_automata_contrasenas():
    # Estados
    estados = {'q0', 'q1', 'q2', 'q4'}
    
    # Alfabeto
    mayusculas = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    minusculas = set("abcdefghijklmnopqrstuvwxyz")
    digitos = set("0123456789")
    alfabeto = mayusculas.union(minusculas).union(digitos)
    
    # Transiciones (AFN - puede tener múltiples destinos)
    transiciones = {}
    
    # q0: estado inicial - transición con mayúsculas a q1 y q4
    for letra in mayusculas:
        transiciones[('q0', letra)] = {'q1', 'q4'}
    
    # q1: puede recibir minúsculas (vuelve a q1) o dígitos (va a q2)
    for letra in minusculas:
        transiciones[('q1', letra)] = {'q1'}
    for digito in digitos:
        transiciones[('q1', digito)] = {'q2'}
    
    # q4: recibe dígitos y va a q2
    for digito in digitos:
        transiciones[('q4', digito)] = {'q2'}
    
    # q2: estado de dígitos - puede recibir más dígitos
    for digito in digitos:
        transiciones[('q2', digito)] = {'q2'}
    
    estado_inicial = 'q0'
    estados_aceptacion = {'q2'}
    
    return AFN(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def main():
    automata = crear_automata_contrasenas()
    
    print("=== AFN - VALIDACIÓN DE CONTRASEÑAS TEMPORALES ===")
    print("Formato: Letra mayúscula + [letras minúsculas opcionales] + dígitos obligatorios")
    print("Ejemplos válidos: 'A123', 'Password123', 'X99'")
    print("Ejemplos inválidos: 'soga2025', 'A1', '1234'")
    print()
    
    while True:
        cadena = input("Ingrese una contraseña (o 'salir' para terminar): ").strip()
        
        if cadena.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Verificar que todos los caracteres sean válidos
        caracteres_validos = all(c in automata.alfabeto for c in cadena)
        if not caracteres_validos:
            print("Error: La cadena contiene caracteres no permitidos")
            print("Solo se permiten: A-Z, a-z, 0-9")
            continue
        
        resultado = automata.procesar_cadena(cadena)
        
        if resultado:
            print(f"✓ La contraseña '{cadena}' ES VÁLIDA")
        else:
            print(f"✗ La contraseña '{cadena}' NO ES VÁLIDA")
        
        print()

if __name__ == "__main__":
    main()