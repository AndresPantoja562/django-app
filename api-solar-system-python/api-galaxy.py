<<<<<<< HEAD
import requests
import os

def get_data(body_type):
    os.system("clear") # Limpiar pantalla
    print("::: INFORMACIÓN DEL SISTEMA SOLAR :::")
    api_url = f"https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=bodyType,{body_type}"

    try:
        # Hacer la solicitud a la API
        response = requests.get(api_url)
        response.raise_for_status() # Manejar errores
    
        data = response.json()

        # if body_type == "planet":
        #     for body in data["bodies"]:
        #         if body["isPlanet"]:
        #             print("Nombre en inglés:", body["englishName"])
        #             print("Gravedad:", body["gravity"])
        #             print("Inclinación:", body["inclination"])
        #             print("¿Es un planeta?", body["isPlanet"])
        #             print("\n")
        # if body_type == "moon":  # Añadido para los cometas
        #     for body in data["bodies"]:
        #         if (body["isPlanet"]== False):
        #             print("Nombre en inglés:", body["englishName"])
        #             print("Gravedad:", body["gravity"])
        #             print("Inclinación:", body["inclination"])
        #             print("¿Es un planeta?", body["isPlanet"])
        #             print("\n")
        if body_type == "asteroid":  # Añadido para los cometas
            for body in data["bodies"]:
                if not body["isPlanet"]:
                    print("Nombre en inglés:", body["englishName"])
                    print("Gravedad:", body["gravity"])
                    print("Inclinación:", body["inclination"])
                    print("¿Es un planeta?", body["isPlanet"])
                    print("\n")

        else:
            print("Datos no disponibles para la opción seleccionada.")

    except requests.exceptions.RequestException as e:
        print(f"Error de la API: {e}")

def main():
    while True:
        body_type = None
        print("#### MENÚ PRINCIPAL ####")
        print("[1]. Planetas")
        print("[2]. Lunas")
        print("[3]. Estrellas")
        print("[4]. Asteroides")
        print("[5]. Cometas")
        print("[6]. Salir")

        opt = input("::: Elija una opción: ")

        if opt == '1':
            body_type = "planet"
        elif opt == '2':
            body_type = "moon"
        elif opt == '3':
            body_type = "star"
        elif opt == '4':
            body_type = "asteroid"
        elif opt == '5':
            body_type = "comet"
        elif opt == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija de nuevo.")
            continue

        get_data(body_type)

if __name__ == "__main__":
    main()
=======
import requests #Let 'u get data from api-url
import os #Let 'u execute os commands

def get_data():
    os.system("clear") #Clear screen
    print("::: SOLAR SYSTEM INFORMATION :::")
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try:
        #Request to API
        response = requests.get(api_url)
        response.raise_for_status() #Read errors
    
        data = response.json()

        print("#### Main menu ####")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Comets")
        print("[6]. Exit")
        opt = input("::: Press any option: ")

        return data
    except requests.exceptions.RequestException as e:
        print(f"API error {e}") #=> print("API error ",e)


#Main
info = get_data()
print(info)

>>>>>>> 93743bc2d4eeb77d9265f13839b1f851c3e93a50
