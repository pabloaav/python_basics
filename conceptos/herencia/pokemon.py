from typing import Optional


class Pokemon:
    def __init__(self, nombre: str, nivel: int, salud: float):
        self.__nombre = nombre  # nombre es inmutable una vez creado el Pokemon
        self.__esta_vivo = True  # inicializar antes de salud ya que salud lo modifica
        self.nivel = nivel      # usa el setter
        self.salud = salud     # usa el setter

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del Pokémon"""
        return self.__nombre

    @property
    def nivel(self) -> int:
        """Obtiene el nivel del Pokémon"""
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel: int):
        """Establece el nivel del Pokémon"""
        if nivel > 0:
            self.__nivel = nivel
        else:
            print("❌ El nivel debe ser mayor a 0")

    @property
    def salud(self) -> float:
        """Obtiene la salud actual del Pokémon"""
        return self.__salud

    @salud.setter
    def salud(self, salud: float):
        """Establece la salud del Pokémon"""
        if salud < 0:
            self.__salud = 0
            self.__esta_vivo = False
        else:
            self.__salud = salud

    @property
    def esta_vivo(self) -> bool:
        """Verifica si el Pokémon está vivo"""
        return self.__esta_vivo

    def atacar(self, objetivo=None):
        """Ataque básico del Pokémon"""
        if not self.__esta_vivo:
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return 0

        danio = self.__nivel * 2
        print(f"💥 {self.nombre} ataca y genera {danio} de daño")

        if objetivo:
            objetivo.recibir_danio(danio)
        return danio

    def recibir_danio(self, danio: float):
        """Recibe daño y actualiza la salud"""
        self.salud = max(0, self.salud - danio)
        print(f"💫 {self.nombre} recibe {danio} de daño. Salud: {self.salud}")
