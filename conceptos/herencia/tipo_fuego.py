from abc import ABC, abstractmethod
from pokemon import Pokemon


class TipoFuego(Pokemon, ABC):
    tipo = "Fuego"

    def __init__(self, nombre: str, nivel: int, salud: float, temperatura: float):
        super().__init__(nombre, nivel, salud)
        self.temperatura = temperatura  # usa el setter

    @property
    def temperatura(self) -> float:
        """Obtiene la temperatura del Pokémon de fuego"""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura: float):
        """Establece la temperatura del Pokémon de fuego"""
        if temperatura >= 0:
            self.__temperatura = temperatura
        else:
            print("❌ La temperatura no puede ser negativa")

    def lanzallamas(self, objetivo=None):
        """Ataque especial de tipo fuego"""
        danio = self.nivel * 3 + self.temperatura / 5
        print(f"🔥 {self.nombre} usa Lanzallamas! ({danio} daño)")
        if objetivo:
            objetivo.recibir_danio(danio)
        return danio
