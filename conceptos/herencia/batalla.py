# Ejemplo de uso de las clases Pokemon
from pikachu import Pikachu
from charmander import Charmander
from squirtle import Squirtle


def main():
    # Crear diferentes Pokémon
    pika = Pikachu("Sparky", 10, 100, 1000)
    char = Charmander("Flamito", 12, 110, 800)
    squi = Squirtle("Bubbles", 11, 120, 500)

    print("=== DEMOSTRACIÓN DE HERENCIA ===")
    print(f"\n{pika.nombre} - Tipo: {pika.tipo}")
    print(f"Nivel: {pika.nivel}, Salud: {pika.salud}, Voltaje: {pika.voltaje}")

    print(f"\n{char.nombre} - Tipo: {char.tipo}")
    print(
        f"Nivel: {char.nivel}, Salud: {char.salud}, Temperatura: {char.temperatura}")

    print(f"\n{squi.nombre} - Tipo: {squi.tipo}")
    print(f"Nivel: {squi.nivel}, Salud: {squi.salud}, Presión: {squi.presion}")

    print("\n=== BATALLA DE PRUEBA ===")
    # Usar ataque básico (heredado de Pokemon)
    pika.atacar(char)

    # Usar ataques especiales (específicos de cada tipo)
    char.lanzallamas(pika)
    squi.pistola_agua(char)
    pika.impactrueno(squi)


if __name__ == "__main__":
    main()
