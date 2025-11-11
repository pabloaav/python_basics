from tipo_electrico import TipoElectrico


class Jolteon(TipoElectrico):
    """Pokémon tipo eléctrico Jolteon, evolución de Eevee.
    Se caracteriza por su alta velocidad y capacidad de generar electricidad estática"""

    def __init__(self, nombre: str, nivel: int, salud: float, voltaje: float):
        super().__init__(nombre, nivel, salud, voltaje)
        self.__carga_estatica = 0  # Capacidad única de Jolteon

    @property
    def carga_estatica(self) -> int:
        """Obtiene la carga estática acumulada"""
        return self.__carga_estatica

    @carga_estatica.setter
    def carga_estatica(self, valor: int):
        """Establece la carga estática acumulada"""
        if isinstance(valor, int) and valor >= 0:
            self.__carga_estatica = valor
        else:
            print("❌ La carga estática debe ser un número entero no negativo")

    def rayo_carga(self, objetivo=None):
        """Ataque especial único de Jolteon: aumenta su carga estática"""
        if not self.esta_vivo:
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return 0

        self.__carga_estatica += 1
        # El daño aumenta con la carga estática acumulada
        danio = (self.nivel * 2.5 + self.voltaje / 8) * \
            (1 + self.__carga_estatica * 0.2)
        print(f"⚡⚡ {self.nombre} usa Rayo Carga! ({danio} daño)")
        print(f"La carga estática aumenta a {self.__carga_estatica}")

        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
