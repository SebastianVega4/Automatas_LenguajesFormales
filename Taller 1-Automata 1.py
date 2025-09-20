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
            if transicion not in self.transiciones or self.transiciones[transicion] is None:
                return False
            
            estado_actual = self.transiciones[transicion]
        
        return estado_actual in self.estados_aceptacion

def crear_automata_M1():
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
    alfabeto = {'a', 'b'}
    
    transiciones = {
        ('q0', 'a'): 'q2',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): None,
        ('q2', 'a'): 'q4',
        ('q2', 'b'): 'q3',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): None,
        ('q4', 'a'): 'q4',
        ('q4', 'b'): 'q5',
        ('q5', 'a'): 'q4',
        ('q5', 'b'): None
    }
    
    estado_inicial = 'q0'
    estados_aceptacion = {'q4'}
    
    return AFD(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def main():
    automata = crear_automata_M1()
    
    print("=== AUTÓMATA M1 - LENGUAJE L1 ===")
    print("Reconoce: {w ∈ {a,b}* | #a(w) ≥ 2 ∧ bb ∉ w ∧ w termina en a}")
    print()
    
    while True:
        cadena = input("Ingrese una cadena (o 'salir' para terminar): ").strip().lower()
        
        if cadena == 'salir':
            print("¡Hasta luego!")
            break
        
        if not all(c in {'a', 'b'} for c in cadena):
            print("Error: La cadena solo puede contener los símbolos 'a' y 'b'")
            continue
        
        resultado = automata.procesar_cadena(cadena)
        
        if resultado:
            print(f"✓ La cadena '{cadena}' ES ACEPTADA por el autómata M1")
        else:
            print(f"✗ La cadena '{cadena}' NO ES ACEPTADA por el autómata M1")
        
        print()

if __name__ == "__main__":
    main()