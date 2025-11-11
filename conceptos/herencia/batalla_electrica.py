from pikachu import Pikachu
from jolteon import Jolteon


def mostrar_estado(pokemon):
    """Muestra el estado actual del Pokémon"""
    print(f"\n📊 Estado de {pokemon.nombre}:")
    print(f"   Salud: {pokemon.salud}")
    if isinstance(pokemon, Pikachu):
        print(f"   Carga en mejillas: {pokemon.carga_mejillas}")
    elif isinstance(pokemon, Jolteon):
        print(f"   Carga estática: {pokemon.carga_estatica}")
    print(f"   Voltaje: {pokemon.voltaje}")


def batalla_electrica():
    # Crear los combatientes
    pikachu = Pikachu("Sparky", nivel=15, salud=120, voltaje=1000)
    jolteon = Jolteon("Volt", nivel=15, salud=120, voltaje=1000)

    print("=== ⚡ BATALLA ELÉCTRICA ⚡ ===")
    print(f"{pikachu.nombre} VS {jolteon.nombre}")
    print("\nComienza el combate!")

    # Ronda 1
    print("\n📍 Ronda 1:")
    pikachu.ataque_rapido(jolteon)  # Pikachu usa su ataque especial
    mostrar_estado(jolteon)
    jolteon.rayo_carga(pikachu)     # Jolteon contraataca
    mostrar_estado(pikachu)

    # Ronda 2
    print("\n📍 Ronda 2:")
    pikachu.impactrueno(jolteon)    # Pikachu usa ataque común
    mostrar_estado(jolteon)
    jolteon.impactrueno(pikachu)    # Jolteon usa ataque común
    mostrar_estado(pikachu)

    # Ronda 3
    print("\n📍 Ronda 3:")
    # Pikachu usa ataque especial (más fuerte por carga)
    pikachu.ataque_rapido(jolteon)
    mostrar_estado(jolteon)
    # Jolteon usa ataque especial (más fuerte por carga)
    jolteon.rayo_carga(pikachu)
    mostrar_estado(pikachu)

    # Estado final
    print("\n=== 🏁 FIN DE LA BATALLA ===")
    print("\nEstado final de los combatientes:")
    mostrar_estado(pikachu)
    mostrar_estado(jolteon)

    # Determinar ganador
    if pikachu.salud > jolteon.salud:
        print(f"\n🏆 ¡{pikachu.nombre} es el ganador!")
    elif jolteon.salud > pikachu.salud:
        print(f"\n🏆 ¡{jolteon.nombre} es el ganador!")
    else:
        print("\n🤝 ¡Es un empate!")


if __name__ == "__main__":
    batalla_electrica()
