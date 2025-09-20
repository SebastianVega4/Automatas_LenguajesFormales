from colorama import Fore, Style, init
import string

init(autoreset=True)

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
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'}
    
    # Alfabeto
    letras = set("abcdefghijklmnopqrstuvwxyz")
    digitos = set("0123456789")
    caracteres_especiales = {'@', '.'}
    alfabeto = letras.union(digitos).union(caracteres_especiales)
    
    transiciones = {}
    
    # q0: solo acepta letras minúsculas
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

def validar_formato_basico(correo):
    if '@' not in correo:
        return False, "El correo debe contener '@'"
    
    if not correo.split('@')[0]:  # Parte antes del @
        return False, "El correo debe tener texto antes del '@'"
    
    if not correo.endswith('@uptc.edu.co'):
        return False, "El correo debe terminar con '@uptc.edu.co'"
    
    # Verificar que el inicio sea con letra minúscula
    if not correo[0].islower() or not correo[0].isalpha():
        return False, "El correo debe comenzar con una letra minúscula"
    
    return True, "Formato válido"

def main():
    automata = crear_automata_correos()
    
    print()    
    print()
    print(f"{Fore.CYAN}==================== AFD - VALIDACIÓN DE CORREOS INSTITUCIONALES ====================")
    print(f"Formato: [letras/dígitos] + @uptc.edu.co")
    print(f"Debe comenzar con letra minúscula")
    print(f"Ejemplos válidos: 'juan3@uptc.edu.co', 'maria@uptc.edu.co'")
    print(f"Ejemplos inválidos: '123juan@uptc.edu.co', 'MARIA@uptc.edu.co'{Style.RESET_ALL}")
    print(f"{Fore.CYAN}====================================================================================")
    print()
    
    # Casos de prueba
    casos_validos = ['juan3@uptc.edu.co', 'maria@uptc.edu.co', 'abc123@uptc.edu.co', 'a@uptc.edu.co']
    casos_invalidos = ['123juan@uptc.edu.co', 'MARIA@uptc.edu.co', 'juan@uptc.com', 
                      '@uptc.edu.co', 'juan@uptc.edu.com', 'JUAN@uptc.edu.co']
    
    print(f"{Fore.YELLOW}=== CASOS DE PRUEBA VÁLIDOS ===")
    for correo in casos_validos:
        resultado = automata.procesar_cadena(correo)
        color = Fore.GREEN if resultado else Fore.RED
        simbolo = "✓" if resultado else "✗"
        print(f"{color}{simbolo} '{correo}' -> {'VÁLIDO' if resultado else 'INVÁLIDO'}{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}=== CASOS DE PRUEBA INVÁLIDOS ===")
    for correo in casos_invalidos:
        resultado = automata.procesar_cadena(correo)
        color = Fore.RED if not resultado else Fore.GREEN
        simbolo = "✓" if resultado else "✗"
        print(f"{color}{simbolo} '{correo}' -> {'VÁLIDO' if resultado else 'INVÁLIDO'}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}=== VALIDACIÓN DE ENTRADAS ===")
    
    while True:
        correo = input("\nIngrese un correo electrónico (o 'salir' para terminar): ").strip().lower()
        
        if correo.lower() == 'salir':
            print(f"{Fore.BLUE}¡Hasta luego!{Style.RESET_ALL}")
            break
        
        formato_valido, mensaje = validar_formato_basico(correo)
        if not formato_valido:
            print(f"{Fore.RED}✗ {mensaje}{Style.RESET_ALL}")
            continue
        
        caracteres_validos = all(c in automata.alfabeto for c in correo)
        if not caracteres_validos:
            print(f"{Fore.RED}Error: El correo contiene caracteres no permitidos{Style.RESET_ALL}")
            print(f"{Fore.RED}Solo se permiten: a-z, 0-9, @, .{Style.RESET_ALL}")
            continue
        
        resultado = automata.procesar_cadena(correo)
        
        if resultado:
            print(f"{Fore.GREEN}✓ El correo '{correo}' ES VÁLIDO{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ El correo '{correo}' NO ES VÁLIDO{Style.RESET_ALL}")
        
        print()

if __name__ == "__main__":
    main()