from automata.fa.dfa import DFA
from colorama import Fore, Style, init
import string

init(autoreset=True)

def crear_automata_M2():   
    # Definición formal del autómata
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q_reject'}
    letras = set(string.ascii_uppercase)
    digitos = set(string.digits)
    alfabeto = letras.union(digitos)
    estado_inicial = 'q0'
    estados_aceptacion = {'q9'}
    
    # Construir la función de transición
    transiciones = {
        'q0': {},
        'q1': {},
        'q2': {},
        'q3': {},
        'q4': {},
        'q5': {},
        'q6': {},
        'q7': {},
        'q8': {},
        'q9': {},
        'q_reject': {}  # Estado de rechazo es decir inválidas
    }
    
    # Llenar todas las transiciones con estado de rechazo por defecto
    for estado in estados:
        for simbolo in alfabeto:
            transiciones[estado][simbolo] = 'q_reject'
    
    # Primera letra (q0 -> q1)
    for letra in letras:
        transiciones['q0'][letra] = 'q1'
    
    # Segunda letra (q1 -> q2)
    for letra in letras:
        transiciones['q1'][letra] = 'q2'
    
    # Primer dígito (q2 -> q3 o q4)
    for digito in digitos:
        if digito == '0':
            transiciones['q2'][digito] = 'q3'
        else:
            transiciones['q2'][digito] = 'q4'
    
    # Segundo dígito desde q3 (primer dígito fue 0)
    for digito in digitos:
        if digito == '0':
            transiciones['q3'][digito] = 'q_reject'  # Prohibido: "00"
        else:
            transiciones['q3'][digito] = 'q5'
    
    # Segundo dígito desde q4 (primer dígito fue 1-9)
    for digito in digitos:
        if digito == '0':
            transiciones['q4'][digito] = 'q6'
        else:
            transiciones['q4'][digito] = 'q7'
    
    # Tercer dígito desde q5 (secuencia: 0X  X≠0)
    for digito in digitos:
        transiciones['q5'][digito] = 'q8'
    
    # Tercer dígito desde q6 (secuencia: X0  X≠0)
    for digito in digitos:
        if digito == '0':
            transiciones['q6'][digito] = 'q_reject'  # Prohibido: "X00"
        else:
            transiciones['q6'][digito] = 'q8'
    
    # Tercer dígito desde q7 (secuencia: XY X≠0, Y≠0)
    for digito in digitos:
        transiciones['q7'][digito] = 'q8'
    
    # Última letra (q8 -> q9)
    for letra in letras:
        transiciones['q8'][letra] = 'q9'
    
    # Estado q9 solo va a q_reject (cadena demasiado larga)
    for simbolo in alfabeto:
        transiciones['q9'][simbolo] = 'q_reject'
    
    # Crear el DFA automata-lib
    automata = DFA(
        states=estados,
        input_symbols=alfabeto,
        transitions=transiciones,
        initial_state=estado_inicial,
        final_states=estados_aceptacion
    )
    
    return automata

def validar_cadena_M2(automata, cadena):
    try:
        return automata.accepts_input(cadena)
    except:
        return False

def validar_formato_basico(cadena):
    if len(cadena) != 6:
        return False, "El código debe tener exactamente 6 caracteres"
    
    # Verificar que los primeros dos caracteres sean letras MAYÚSCULAS
    if not cadena[0].isalpha() or not cadena[1].isalpha():
        return False, "Los dos primeros caracteres deben ser letras"
    if not cadena[0].isupper() or not cadena[1].isupper():
        return False, "Las dos primeras letras deben ser MAYÚSCULAS"
    
    # Verificar que los siguientes tres caracteres sean dígitos
    if not cadena[2].isdigit() or not cadena[3].isdigit() or not cadena[4].isdigit():
        return False, "Los caracteres 3-5 deben ser dígitos"
    
    # Verificar que el último carácter sea letra MAYÚSCULA
    if not cadena[5].isalpha():
        return False, "El último carácter debe ser una letra"
    if not cadena[5].isupper():
        return False, "La última letra debe ser MAYÚSCULA"
    
    # Verificar que no haya minúsculas en toda la cadena
    if any(c.islower() for c in cadena):
        return False, "El código no puede contener letras minúsculas"
    
    return True, "Formato válido"

def main():
    automata = crear_automata_M2()
    
    print()
    print()
    print(f"{Fore.CYAN}====================================AUTÓMATA M2====================================")
    print(f"Formato: 2 letras MAYÚSCULAS + 3 dígitos + 1 letra MAYÚSCULA")
    print(f"Restricción: No pueden haber dos ceros consecutivos en los 3 dígitos centrales")
    print(f"Ejemplos válidos: AB123Z, XY019A, PQ507B")
    print(f"Ejemplos inválidos: AB001Z, XY100A, ab123C, AB123c{Style.RESET_ALL}")
    print(f"{Fore.CYAN}====================================================================================")
    print()

    while True:
        cadena = input("\nIngrese un código POS (o 'salir' para terminar): ").strip()
        
        if cadena.lower() == 'salir':
            print(f"{Fore.BLUE}¡Hasta luego!{Style.RESET_ALL}")
            break
        
        
        # Validación básica de formato
        formato_valido, mensaje = validar_formato_basico(cadena)
        if not formato_valido:
            print(f"{Fore.RED}✗ {mensaje}{Style.RESET_ALL}")
            continue
        
        # Validación con el autómata
        resultado = validar_cadena_M2(automata, cadena)
        
        if resultado:
            print(f"{Fore.GREEN}✓ El código '{cadena}' ES VÁLIDO{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ El código '{cadena}' NO ES VÁLIDO (contiene ceros consecutivos){Style.RESET_ALL}")

if __name__ == "__main__":
    main()