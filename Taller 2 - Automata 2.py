class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
    
    def procesar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False
            
            transicion = (estado_actual, simbolo)
            if transicion not in self.transiciones:
                return False
            
            estado_actual = self.transiciones[transicion]
        
        return estado_actual in self.estados_aceptacion

def crear_automata_correos():
    # Estados
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'}
    
    # Alfabeto
    letras = set("abcdefghijklmnopqrstuvwxyz")
    digitos = set("0123456789")
    caracteres_especiales = {'@', '.'}
    alfabeto = letras.union(digitos).union(caracteres_especiales)
    
    # Transiciones (AFD - una única transición por estado y símbolo)
    transiciones = {}
    
    # q0: solo acepta letras minúsculas -> q1
    for letra in letras:
        transiciones[('q0', letra)] = 'q1'
    
    # q1: acepta letras, dígitos (vuelve a q1) o @ -> q2
    for letra in letras:
        transiciones[('q1', letra)] = 'q1'
    for digito in digitos:
        transiciones[('q1', digito)] = 'q1'
    transiciones[('q1', '@')] = 'q2'
    
    # q2: solo acepta 'u' -> q3
    transiciones[('q2', 'u')] = 'q3'
    
    # q3: solo acepta 'p' -> q4
    transiciones[('q3', 'p')] = 'q4'
    
    # q4: solo acepta 't' -> q5
    transiciones[('q4', 't')] = 'q5'
    
    # q5: solo acepta 'c' -> q6
    transiciones[('q5', 'c')] = 'q6'
    
    # q6: solo acepta '.' -> q7
    transiciones[('q6', '.')] = 'q7'
    
    # q7: solo acepta 'e' -> q8
    transiciones[('q7', 'e')] = 'q8'
    
    # q8: solo acepta 'd' -> q9
    transiciones[('q8', 'd')] = 'q9'
    
    # q9: solo acepta 'u' -> q10
    transiciones[('q9', 'u')] = 'q10'
    
    # q10: solo acepta '.' -> q11
    transiciones[('q10', '.')] = 'q11'
    
    # q11: solo acepta 'c' -> q12
    transiciones[('q11', 'c')] = 'q12'
    
    # q12: solo acepta 'o' -> q13
    transiciones[('q12', 'o')] = 'q13'
    
    estado_inicial = 'q0'
    estados_aceptacion = {'q13'}
    
    return AFD(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def main():
    automata = crear_automata_correos()
    
    print("=== AFD - VALIDACIÓN DE CORREOS INSTITUCIONALES ===")
    print("Formato: [letras/dígitos] + @uptc.edu.co")
    print("Debe comenzar con letra minúscula")
    print("Ejemplos válidos: 'juan3@uptc.edu.co', 'maria@uptc.edu.co'")
    print("Ejemplos inválidos: '123juan@uptc.edu.co', 'MARIA@uptc.edu.co'")
    print()
    
    while True:
        correo = input("Ingrese un correo electrónico (o 'salir' para terminar): ").strip().lower()
        
        if correo.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Verificar que todos los caracteres sean válidos
        caracteres_validos = all(c in automata.alfabeto for c in correo)
        if not caracteres_validos:
            print("Error: El correo contiene caracteres no permitidos")
            print("Solo se permiten: a-z, 0-9, @, .")
            continue
        
        resultado = automata.procesar_cadena(correo)
        
        if resultado:
            print(f"✓ El correo '{correo}' ES VÁLIDO")
        else:
            print(f"✗ El correo '{correo}' NO ES VÁLIDO")
        
        print()

if __name__ == "__main__":
    main()