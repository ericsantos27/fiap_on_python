level = input("Nível de acesso: ").upper()
if level == "ADM" or level == "USR":
    genre = input("Gênero: ")
    if level == "ADM":
        if genre == "F":
            print("Olá, administradora")
        else:
            print("Olá, administrador")
    elif level == "USR":
        if genre == "F":
            print("Olá, usuária")
        else:
            print("Olá, usuário")
elif level == "GUEST":
    print("Olá, visitante")
else:
    print("Olá, desconhecido(a)")
