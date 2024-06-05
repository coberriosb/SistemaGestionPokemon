import csv 
import msvcrt 
import os 

pokemones = ""
with open('pokemon_primera_generacion(1).csv',newline='',encoding='utf-8') as a:
    datos = csv.reader(a, delimiter=",")
    pokemones = list(datos)

cinturon = []

while True: 
    print("<< presione para continuar>>")
    msvcrt.getch()
    os.system("cls")

    print("""
    SISTEMA DE GESTION CINTURON POKEMON
    ----------------------------------------
    1) Mostrar pokemon
    2) Buscar pokemon 
    3) Agregar al cinturon 
    4) Mostrar el cinturon 
    5) Quitar del cinturon 
    6) Generar reporte Cinturon en CSV
    0) Salir """)
    opcion = input("Seleccione : ")

    if opcion=="0":
        break 
    elif opcion=="1":
        print("\033[33mListado de pokemones\033[0m")
        for p in pokemones: 
            print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")
    elif opcion=="2":
        print("\033[33mBuscar pokemon\033[0m")
        nombre = input("Ingrese nombre para buscar : ").capitalize()
        centinela = False 
        for p in pokemones:
            if p[1]==nombre: 
                print(f"\033[32mENCONTRADO \n{p[0]}\t{p[1]}\t{p[2]}\tAltura: {p[3]}\tPeso: {p[4]}\033[0m")
                centinela = True
                break
        if not centinela: 
                print("\033[31mPokemon no encontrado\033[0m")
    elif opcion=="3":
        print("\033[33mAgregar al cinturon\033[0m")
        if len(cinturon)<6:
            nombre = input("Ingrese nombre para buscar : ").capitalize()
            centinela = False 
            for p in pokemones:
                if p[1]==nombre: 
                    print(f"\033[32mENCONTRADO \n{p[0]}\t{p[1]}\t{p[2]}\tAltura: {p[3]}\tPeso: {p[4]}\033[0m")
                    repetido = False
                    for pok in cinturon: 
                        if pok[1]==nombre:
                            repetido == True
                    if not repetido: 
                        cinturon.append(p)
                        print("\033[32mpokemon registrado\033[0m")
                    else:
                        print("\033[31mPokemon repetido\033[0m")
                    centinela = True
                    break
            if not centinela: 
                print("\033[31mPokemon no encontrado\033[0m")
        else: 
            print("\033[31mCinturon sin espacio\033[0m")
    elif opcion=="4":
        print("\033[33mMostrar Cinturon\033[0m")
        if len(cinturon)>0:
            for i in range(len(cinturon)): 
                print(f"{i+1} {cinturon[i][1]} {cinturon[i][2]}")
        else:
            print("\033[31mCinturón vacío\033[0m")
    elif opcion=="5":
        print("\033[33mQuitar del cinturon\033[0m")
        nombre = input("Ingrese nombre para quitar: ").capitalize()
        centinela = False #Recordar que centinela es para validar la existencia del pokemon y mostrar si no se encuentra
        for p in cinturon: 
            if p[1]==nombre: 
                cinturon.remove(p)
                print("\033[31mPokemon removido\033[0m")
                centinela = True
                break
        if not centinela:
            print("\033[31mPokemon no encontrado\033[0m")
    elif opcion=="6":
        if len(cinturon)>0: 
            with open('reporte_cinturon.csv','w',newline='',encoding='utf-8') as a: 
                escritura = csv.writer(a, delimiter=',')
                escritura.writerows(cinturon)
        else:
            print("\033[31mNo hay pokemones en el cinturon\033[0m")
    else:
        pass
    