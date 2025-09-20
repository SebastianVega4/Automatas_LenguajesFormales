from automata.fa.dfa import DFA
from colorama import Fore, Style, init

init(autoreset=True)

def crear_automata_M1():
    
    # Definición formal del autómata
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q_reject'}
    alfabeto = {'a', 'b'}
    estado_inicial = 'q0'
    estados_aceptacion = {'q4'}
    
    # Inicializar todas las transiciones con estado de rechazo
    transiciones = {
        'q0': {'a': 'q_reject', 'b': 'q_reject'},
        'q1': {'a': 'q_reject', 'b': 'q_reject'},
        'q2': {'a': 'q_reject', 'b': 'q_reject'},
        'q3': {'a': 'q_reject', 'b': 'q_reject'},
        'q4': {'a': 'q_reject', 'b': 'q_reject'},
        'q5': {'a': 'q_reject', 'b': 'q_reject'},
        'q_reject': {'a': 'q_reject', 'b': 'q_reject'}
    }
    
    # Definir las transiciones válidas
    transiciones['q0']['a'] = 'q2'
    transiciones['q0']['b'] = 'q1'
    
    transiciones['q1']['a'] = 'q2'
    transiciones['q1']['b'] = 'q_reject'  # "bb" no permitido
    
    transiciones['q2']['a'] = 'q4'
    transiciones['q2']['b'] = 'q3'
    
    transiciones['q3']['a'] = 'q4'
    transiciones['q3']['b'] = 'q_reject'  # "bb" no permitido
    
    transiciones['q4']['a'] = 'q4'
    transiciones['q4']['b'] = 'q5'
    
    transiciones['q5']['a'] = 'q4'
    transiciones['q5']['b'] = 'q_reject'  # "bb" no permitido
    
    # Crear el DFA automata-lib
    automata = DFA(
        states=estados,
        input_symbols=alfabeto,
        transitions=transiciones,
        initial_state=estado_inicial,
        final_states=estados_aceptacion
    )
    
    return automata

def validar_cadena_M1(automata, cadena):
    try:
        return automata.accepts_input(cadena)
    except:
        return False

def main():
    automata = crear_automata_M1()
    
    print()
    print(f"{Fore.CYAN}=== AUTÓMATA M1 - LENGUAJE L1 ===")
    print(f"Reconoce: {{w ∈ {{a,b}}* | #a(w) ≥ 2 ∧ bb ∉ w ∧ w termina en a}}")
    print()

    
    while True:
        cadena = input("\nIngrese una cadena (o 'salir' para terminar): ").strip().lower()
        
        if cadena == 'salir':
            print(f"{Fore.BLUE}¡Hasta luego!{Style.RESET_ALL}")
            break
        
        if not all(c in {'a', 'b'} for c in cadena):
            print(f"{Fore.RED}Error: La cadena solo puede contener los símbolos 'a' y 'b'{Style.RESET_ALL}")
            continue
        
        resultado = validar_cadena_M1(automata, cadena)
        
        if resultado:
            print(f"{Fore.GREEN}✓ La cadena '{cadena}' ES ACEPTADA por el autómata M1{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ La cadena '{cadena}' NO ES ACEPTADA por el autómata M1{Style.RESET_ALL}")

if __name__ == "__main__":
    main()