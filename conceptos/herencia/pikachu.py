from tipo_electrico import TipoElectrico


class Pikachu(TipoElectrico):
    """Pokémon tipo eléctrico Pikachu.
    Se caracteriza por poder almacenar electricidad en sus mejillas"""

    def __init__(self, nombre: str, nivel: int, salud: float, voltaje: float):
        super().__init__(nombre, nivel, salud, voltaje)
        self.__carga_mejillas = 0  # Capacidad única de Pikachu

    @property
    def carga_mejillas(self) -> int:
        """Obtiene la carga almacenada en las mejillas"""
        return self.__carga_mejillas

    @carga_mejillas.setter
    def carga_mejillas(self, valor: int):
        """Establece la carga almacenada en las mejillas"""
        if isinstance(valor, int) and valor >= 0:
            self.__carga_mejillas = valor
        else:
            print("❌ La carga en las mejillas debe ser un número entero no negativo")

    def ataque_rapido(self, objetivo=None):
        """Ataque especial único de Pikachu: almacena carga en sus mejillas"""
        if not self.esta_vivo:
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return 0

        self.__carga_mejillas += 1
        # El daño base es menor pero gana bonus por carga en mejillas
        danio = (self.nivel * 1.5 + self.voltaje / 12) * \
            (1 + self.__carga_mejillas * 0.3)
        print(f"⚡ {self.nombre} usa Ataque Rápido! ({danio} daño)")
        print(f"La carga en sus mejillas aumenta a {self.__carga_mejillas}")

        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
