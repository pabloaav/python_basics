from pokemon import Pokemon


class Squirtle(Pokemon):
    tipo = "Agua"

    def __init__(self, nombre: str, nivel: int, salud: float, presion: float):
        super().__init__(nombre, nivel, salud)
        self.__presion = presion

    @property
    def presion(self) -> float:
        """Obtiene la presión de agua de Squirtle"""
        return self.__presion

    def pistola_agua(self, objetivo=None):
        """Ataque especial de tipo agua"""
        danio = self.nivel * 2.5 + self.presion / 2
        print(f"💧 {self.nombre} usa Pistola Agua! ({danio} daño)")
        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
