from colorama import Fore, Style, init
import string

init(autoreset=True)

class AFN:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
    
    def procesar_cadena(self, cadena):
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
        
        return any(estado in self.estados_aceptacion for estado in estados_actuales)

def crear_automata_contrasenas():
    # Estados
    estados = {'q0', 'q1', 'q2', 'q4'}
    
    # Alfabeto
    mayusculas = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    minusculas = set("abcdefghijklmnopqrstuvwxyz")
    digitos = set("0123456789")
    alfabeto = mayusculas.union(minusculas).union(digitos)
    
    transiciones = {}
    
    # q0: estado inicial - mayúsculas a q1 y q4
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
    
    print()
    print()
    print(f"{Fore.CYAN}==================== AFN - VALIDACIÓN DE CONTRASEÑAS TEMPORALES ====================")
    print(f"Formato: Letra mayúscula + [letras minúsculas opcionales] + dígitos obligatorios")
    print(f"Ejemplos válidos: 'A123', 'Password123', 'X99'")
    print(f"Ejemplos inválidos: 'soga2025', 'A1', '1234'{Style.RESET_ALL}")
    print(f"{Fore.CYAN}====================================================================================")
    print()
    
    # Casos de prueba
    casos_validos = ['A123', 'Password123', 'X99', 'B456', 'Helloworld2023']
    casos_invalidos = ['soga2025', 'A198k', '1234', 'abc123', 'TEST', 'A', '123']
    
    print(f"{Fore.YELLOW}=== CASOS DE PRUEBA VÁLIDOS ===")
    for cadena in casos_validos:
        resultado = automata.procesar_cadena(cadena)
        color = Fore.GREEN if resultado else Fore.RED
        simbolo = "✓" if resultado else "✗"
        print(f"{color}{simbolo} '{cadena}' -> {'VÁLIDA' if resultado else 'INVÁLIDA'}{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}=== CASOS DE PRUEBA INVÁLIDOS ===")
    for cadena in casos_invalidos:
        resultado = automata.procesar_cadena(cadena)
        color = Fore.RED if not resultado else Fore.GREEN
        simbolo = "✓" if resultado else "✗"
        print(f"{color}{simbolo} '{cadena}' -> {'VÁLIDA' if resultado else 'INVÁLIDA'}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}=== VALIDACIÓN DE ENTRADAS ===")
    
    while True:
        cadena = input("\nIngrese una contraseña (o 'salir' para terminar): ").strip()
        
        if cadena.lower() == 'salir':
            print(f"{Fore.BLUE}¡Hasta luego!{Style.RESET_ALL}")
            break
        
        caracteres_validos = all(c in automata.alfabeto for c in cadena)
        if not caracteres_validos:
            print(f"{Fore.RED}Error: La cadena contiene caracteres no permitidos{Style.RESET_ALL}")
            print(f"{Fore.RED}Solo se permiten: A-Z, a-z, 0-9{Style.RESET_ALL}")
            continue
        
        resultado = automata.procesar_cadena(cadena)
        
        if resultado:
            print(f"{Fore.GREEN}✓ La contraseña '{cadena}' ES VÁLIDA{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ La contraseña '{cadena}' NO ES VÁLIDA{Style.RESET_ALL}")
        
        print()

if __name__ == "__main__":
    main()