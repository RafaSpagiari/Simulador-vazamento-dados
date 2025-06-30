import time

# Lista simulada de dados vazados 
vazamentos_simulados = {
    "rafaspagiari3108@gmail.com" : ["Twitter (2021), Adobe (2013)"],
    "testepython@gmail.com" : ["Facebook (2019)"],
    "rafaemailfake@gmail.com" : ["Yahoo (2013), Canva (2019)"],
}

def verificar_email(email): 
    print (f"\n Verificando vazamentos para: {email}...")
    time.sleep (1.5)  # simula tempo de resposta

    if email in vazamentos_simulados:
        print("Vazamentos encontrados:")
        for vazamento in vazamentos_simulados[email]:
            print(f" - {vazamento}")
    else:
        print ("Nnenhum vazamento encontrado para este email.")

def menu():
    print ("\n=== Simulador de Vazamentos de Dados ===")
    while True: 
        email = input("\nDigite um email para verificar (ou 'sair' para encerrar): ").strip()
        if email.lower() == "sair":
            print("Encerrando o simulador.")
            break 
        verificar_email(email)
            

# Iniciar o programa 
if __name__ == "__main__":
    menu()