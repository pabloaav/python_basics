from pokemon import Pokemon


class Squirtle(Pokemon):
    tipo = "Agua"

    def __init__(self, nombre: str, nivel: int, salud: float, presion: float):
        super().__init__(nombre, nivel, salud)
        self.presion = presion  # usa el setter

    @property
    def presion(self) -> float:
        """Obtiene la presión de agua de Squirtle"""
        return self.__presion

    @presion.setter
    def presion(self, presion: float):
        """Establece la presión de agua de Squirtle"""
        if presion >= 0:
            self.__presion = presion
        else:
            print("❌ La presión no puede ser negativa")

    def pistola_agua(self, objetivo=None):
        """Ataque especial de tipo agua"""
        danio = self.nivel * 2.5 + self.presion / 2
        print(f"💧 {self.nombre} usa Pistola Agua! ({danio} daño)")
        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
