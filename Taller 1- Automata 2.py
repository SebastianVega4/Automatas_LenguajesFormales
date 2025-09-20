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

def crear_automata_M2():
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'}
    letras = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digitos = set("0123456789")
    alfabeto = letras.union(digitos)
    
    transiciones = {}
    
    # Primera letra (q0 -> q1)
    for letra in letras:
        transiciones[('q0', letra)] = 'q1'
    
    # Segunda letra (q1 -> q2)
    for letra in letras:
        transiciones[('q1', letra)] = 'q2'
    
    # Primer dígito (q2 -> q3 o q4)
    for digito in digitos:
        if digito == '0':
            transiciones[('q2', '0')] = 'q3'
        else:
            transiciones[('q2', digito)] = 'q4'
    
    # Segundo dígito desde q3 (primer dígito fue 0)
    for digito in digitos:
        if digito == '0':
            transiciones[('q3', '0')] = None  # Prohibido: "00"
        else:
            transiciones[('q3', digito)] = 'q5'
    
    # Segundo dígito desde q4 (primer dígito fue 1-9)
    for digito in digitos:
        if digito == '0':
            transiciones[('q4', '0')] = 'q6'
        else:
            transiciones[('q4', digito)] = 'q7'
    
    # Tercer dígito desde q5 (secuencia: 0X donde X≠0)
    for digito in digitos:
        transiciones[('q5', digito)] = 'q8'
    
    # Tercer dígito desde q6 (secuencia: X0 donde X≠0)
    for digito in digitos:
        if digito == '0':
            transiciones[('q6', '0')] = None  # Prohibido: "X00"
        else:
            transiciones[('q6', digito)] = 'q8'
    
    # Tercer dígito desde q7 (secuencia: XY donde X≠0, Y≠0)
    for digito in digitos:
        transiciones[('q7', digito)] = 'q8'
    
    # Última letra (q8 -> q9)
    for letra in letras:
        transiciones[('q8', letra)] = 'q9'
    
    estado_inicial = 'q0'
    estados_aceptacion = {'q9'}
    
    return AFD(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def main():
    automata = crear_automata_M2()
    
    print("=== AUTÓMATA M2 - VALIDACIÓN DE CÓDIGOS POS ===")
    print("Formato: 2 letras + 3 dígitos + 1 letra")
    print("Restricción: No pueden haber dos ceros consecutivos en los 3 dígitos centrales")
    print("Ejemplos válidos: AB123Z, XY019A, PQ507B")
    print("Ejemplos inválidos: AB001Z, XY100A")
    print()
    
    while True:
        cadena = input("Ingrese un código POS (o 'salir' para terminar): ").strip().upper()
        
        if cadena == 'SALIR':
            print("¡Hasta luego!")
            break
        
        if len(cadena) != 6:
            print("Error: El código debe tener exactamente 6 caracteres")
            continue
        
        resultado = automata.procesar_cadena(cadena)
        
        if resultado:
            print(f"✓ El código '{cadena}' ES VÁLIDO")
        else:
            print(f"✗ El código '{cadena}' NO ES VÁLIDO")
        
        print()

if __name__ == "__main__":
    main()