from pokemon import Pokemon


class Charmander(Pokemon):
    tipo = "Fuego"

    def __init__(self, nombre: str, nivel: int, salud: float, temperatura: float):
        super().__init__(nombre, nivel, salud)
        self.__temperatura = temperatura

    @property
    def temperatura(self) -> float:
        """Obtiene la temperatura de Charmander"""
        return self.__temperatura

    def lanzallamas(self, objetivo=None):
        """Ataque especial de tipo fuego"""
        danio = self.nivel * 3 + self.temperatura / 5
        print(f"🔥 {self.nombre} usa Lanzallamas! ({danio} daño)")
        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
