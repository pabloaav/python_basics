from pokemon import Pokemon


class Pikachu(Pokemon):
    tipo = "Eléctrico"

    def __init__(self, nombre: str, nivel: int, salud: float, voltaje: float):
        super().__init__(nombre, nivel, salud)
        self.voltaje = voltaje  # usa el setter

    @property
    def voltaje(self) -> float:
        """Obtiene el voltaje de Pikachu"""
        return self.__voltaje

    @voltaje.setter
    def voltaje(self, voltaje: float):
        """Establece el voltaje de Pikachu"""
        if voltaje >= 0:
            self.__voltaje = voltaje
        else:
            print("❌ El voltaje no puede ser negativo")

    def impactrueno(self, objetivo=None):
        """Ataque especial de tipo eléctrico"""
        danio = self.nivel * 3 + self.voltaje / 10
        print(f"⚡ {self.nombre} usa Impactrueno! ({danio} daño)")
        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
