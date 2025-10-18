from typing import Optional


class Pikachu:

    tipo = 'Eléctrico'

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.__nivel = nivel  # ⭐ CAMBIADO A PRIVADO
        self.__salud = salud  # ⭐ CAMBIADO A PRIVADO
        self.__salud_maxima = salud  # ⭐ PRIVADO
        # ⭐ CAMBIADO A PRIVADO (como tenías)
        self.__voltaje_maximo = voltaje_max
        # ⭐ CAMBIADO A PRIVADO (como tenías)
        self.__amperaje_maximo = amperaje_max
        self.color = color
        self.__experiencia = 0  # ⭐ PRIVADO
        self.__esta_vivo = True  # ⭐ PRIVADO

    # ========== GETTERS (para leer atributos privados) ==========

    def get_nivel(self):
        """Obtiene el nivel de Pikachu"""
        return self.__nivel

    def get_salud(self):
        """Obtiene la salud actual de Pikachu"""
        return self.__salud

    def get_salud_maxima(self):
        """Obtiene la salud máxima de Pikachu"""
        return self.__salud_maxima

    def get_voltaje_maximo(self):
        """Obtiene el voltaje máximo de Pikachu"""
        return self.__voltaje_maximo

    def get_amperaje_maximo(self):
        """Obtiene el amperaje máximo de Pikachu"""
        return self.__amperaje_maximo

    def get_experiencia(self):
        """Obtiene la experiencia actual de Pikachu"""
        return self.__experiencia

    def get_esta_vivo(self):
        """Verifica si Pikachu está vivo"""
        return self.__esta_vivo

    # ========== SETTERS (para modificar atributos privados) ==========

    def set_nivel(self, nivel):
        """Establece el nivel de Pikachu (con validación)"""
        if nivel > 0:
            self.__nivel = nivel
        else:
            print("❌ El nivel debe ser mayor a 0")

    def set_salud(self, salud: float) -> Optional[str]:
        """Establece la salud de Pikachu (validación estilo Go con retorno de error)

        Args:
            salud: valor de salud a establecer (float)

        Returns:
            Optional[str]: None si todo OK, string con mensaje de error si falla
        """

        # Validación 1: Verificar que no sea negativa
        if salud < 0:
            return "Error: La salud no puede ser negativa"

        # Validación 2: Verificar que no exceda el máximo permitido (5000)
        if salud > 5000:
            return "Error: La salud no puede exceder 5000"

        # Validación 3: Verificar que no exceda la salud máxima del Pikachu
        if salud > self.__salud_maxima:
            self.__salud = self.__salud_maxima
            return f"Advertencia: Se ajustó de {salud} a {self.__salud_maxima}"

        # Si pasó todas las validaciones, establecer la salud
        self.__salud = salud
        return None  # None significa "sin error" (como en Go)

    def set_voltaje_maximo(self, voltaje):
        """Establece el voltaje máximo (con validación)"""
        if voltaje >= 0:
            self.__voltaje_maximo = voltaje
        else:
            print("❌ El voltaje no puede ser negativo")

    def set_amperaje_maximo(self, amperaje):
        """Establece el amperaje máximo (con validación)"""
        if amperaje >= 0:
            self.__amperaje_maximo = amperaje
        else:
            print("❌ El amperaje no puede ser negativo")

    # ========== MÉTODOS DE ACCIÓN (ACTUALIZADOS para usar getters/setters) ==

    def atacar(self, objetivo=None):
        """Pikachu realiza un ataque eléctrico"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return 0

        danio = (self.__nivel * 4) + (self.__voltaje_maximo / 10)  # ⭐ CAMBIADO
        # ⭐ CAMBIADO
        print(f"⚡ {self.nombre} ataca y genera {self.__nivel / 4:.1f} de daño")

        if objetivo:
            objetivo.recibir_danio(danio)

        return danio

    def recibir_danio(self, danio):
        """Recibe daño y actualiza la salud"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            return

        self.__salud -= danio  # ⭐ CAMBIADO
        # ⭐ CAMBIADO
        print(
            f"💥 {
                self.nombre} recibe {
                danio:.1f} de daño. Salud restante: {
                max(
                    0,
                    self.__salud):.1f}")

        if self.__salud <= 0:  # ⭐ CAMBIADO
            self.__salud = 0  # ⭐ CAMBIADO
            self.__esta_vivo = False  # ⭐ CAMBIADO
            print(f"💀 {self.nombre} ha sido debilitado!")

    def defender(self):
        """Pikachu se defiende reduciendo el daño recibido"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} está debilitado y no puede defenderse.")
            return

        reduccion = self.__nivel * 2  # ⭐ CAMBIADO
        print(
            f"🛡️ {
                self.nombre} se defiende y reduce {reduccion} puntos de daño en el próximo ataque")
        return reduccion

    def curarse(self, cantidad=None):
        """Restaura salud de Pikachu"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} está debilitado. ¡Usa un revivir primero!")
            return

        if cantidad is None:
            cantidad = self.__salud_maxima * 0.5  # ⭐ CAMBIADO

        salud_anterior = self.__salud  # ⭐ CAMBIADO
        self.__salud = min(self.__salud + cantidad,
                           self.__salud_maxima)  # ⭐ CAMBIADO
        salud_recuperada = self.__salud - salud_anterior  # ⭐ CAMBIADO

        # ⭐ CAMBIADO
        print(
            f"💚 {
                self.nombre} se cura {
                salud_recuperada:.1f} puntos. Salud actual: {
                self.__salud:.1f}/{
                    self.__salud_maxima}")

    def impactrueno(self, objetivo):
        """Ataque especial: Impactrueno"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} está debilitado y no puede usar Impactrueno.")
            return 0

        danio = self.__voltaje_maximo / 5 + self.__nivel * 3  # ⭐ CAMBIADO
        print(f"⚡⚡ {self.nombre} usa IMPACTRUENO! Causa {danio:.1f} de daño")

        if objetivo:
            objetivo.recibir_danio(danio)

        return danio

    def rayo(self, objetivo):
        """Ataque especial más poderoso: Rayo"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} está debilitado y no puede usar Rayo.")
            return 0

        if self.__nivel < 10:  # ⭐ CAMBIADO
            # ⭐ CAMBIADO
            print(
                f"❌ {
                    self.nombre} necesita nivel 10 o superior para usar Rayo (nivel actual: {
                    self.__nivel})")
            return 0

        danio = (self.__voltaje_maximo / 3) + \
            (self.__amperaje_maximo / 2) + self.__nivel * 5  # ⭐ CAMBIADO
        print(
            f"⚡⚡⚡ {
                self.nombre} usa RAYO! Causa {
                danio:.1f} de daño devastador!")

        if objetivo:
            objetivo.recibir_danio(danio)

        return danio

    def ganar_experiencia(self, exp):
        """Gana experiencia y sube de nivel si es necesario"""
        if not self.__esta_vivo:  # ⭐ CAMBIADO
            return

        self.__experiencia += exp  # ⭐ CAMBIADO
        print(f"⭐ {self.nombre} gana {exp} puntos de experiencia")

        # Subir de nivel cada 100 puntos de experiencia
        if self.__experiencia >= 100:  # ⭐ CAMBIADO
            self.subir_nivel()

    def subir_nivel(self):
        """Sube de nivel y mejora estadísticas"""
        niveles_ganados = self.__experiencia // 100  # ⭐ CAMBIADO
        self.__experiencia = self.__experiencia % 100  # ⭐ CAMBIADO
        self.__nivel += niveles_ganados  # ⭐ CAMBIADO

        # Aumentar estadísticas
        self.__salud_maxima += 20 * niveles_ganados  # ⭐ CAMBIADO
        self.__salud = self.__salud_maxima  # ⭐ CAMBIADO
        self.__voltaje_maximo += 50 * niveles_ganados  # ⭐ CAMBIADO
        self.__amperaje_maximo += 10 * niveles_ganados  # ⭐ CAMBIADO

        print(f"🎉 ¡{self.nombre} sube al nivel {self.__nivel}!")  # ⭐ CAMBIADO
        # ⭐ CAMBIADO
        print(
            f"   Nuevas estadísticas: Salud: {
                self.__salud_maxima}, Voltaje: {
                self.__voltaje_maximo}, Amperaje: {
                self.__amperaje_maximo}")

    def revivir(self):
        """Revive a Pikachu con el 50% de salud"""
        if self.__esta_vivo:  # ⭐ CAMBIADO
            print(f"{self.nombre} ya está consciente.")
            return

        self.__esta_vivo = True  # ⭐ CAMBIADO
        self.__salud = self.__salud_maxima * 0.5  # ⭐ CAMBIADO
        # ⭐ CAMBIADO
        print(
            f"✨ {
                self.nombre} ha sido revivido con {
                self.__salud:.1f} de salud!")

    def mostrar_estado(self):
        """Muestra el estado actual de Pikachu"""
        estado = "Activo" if self.__esta_vivo else "Debilitado"  # ⭐ CAMBIADO
        print(f"\n📊 Estado de {self.nombre}")
        print(f"   Tipo: {self.tipo}")
        print(f"   Color: {self.color}")
        print(f"   Nivel: {self.__nivel}")  # ⭐ CAMBIADO
        print(f"   Experiencia: {self.__experiencia}/100")  # ⭐ CAMBIADO
        # ⭐ CAMBIADO
        print(f"   Salud: {self.__salud:.1f}/{self.__salud_maxima}")
        print(f"   Voltaje máximo: {self.__voltaje_maximo}")  # ⭐ CAMBIADO
        print(f"   Amperaje máximo: {self.__amperaje_maximo}")  # ⭐ CAMBIADO
        print(f"   Estado: {estado}")

    def __str__(self):
        """Representación en string de Pikachu"""
        return f"{
            self.nombre} (Nivel {
            self.__nivel}) - {
            self.__salud:.1f}/{
                self.__salud_maxima} HP"  # ⭐ CAMBIADO

    def __repr__(self):
        """Representación técnica de Pikachu"""
        return f"Pikachu(nombre='{
            self.nombre}', nivel={
            self.__nivel}, salud={
            self.__salud})"  # ⭐ CAMBIADO


# ========== EJEMPLO DE USO CON GETTERS Y SETTERS ==========
if __name__ == "__main__":
    # Crear Pikachu
    pikachu = Pikachu("Sparky", 5, 100, 1000, 50, "amarillo")

    print("=== DEMOSTRANDO ENCAPSULAMIENTO ===\n")

    # ❌ INCORRECTO: Esto NO funcionará (atributo privado)
    # print(pikachu.__nivel)  # Esto daría error

    # ✅ CORRECTO: Usar getters para leer
    print(f"Nivel actual: {pikachu.get_nivel()}")
    print(f"Salud actual: {pikachu.get_salud()}")
    print(f"Voltaje máximo: {pikachu.get_voltaje_maximo()}")
    print(f"¿Está vivo?: {pikachu.get_esta_vivo()}")

    print("\n--- Intentando modificar con setter ---")

    # ✅ CORRECTO: Usar setters para modificar
    pikachu.set_nivel(10)
    print(f"Nuevo nivel: {pikachu.get_nivel()}")

    # El setter valida que no sea negativo
    print("\n--- Probando validación del setter ---")
    pikachu.set_voltaje_maximo(-500)  # Esto mostrará error
    pikachu.set_voltaje_maximo(2000)  # Esto sí funciona
    print(f"Voltaje después de validación: {pikachu.get_voltaje_maximo()}")

    print("\n=== BATALLA DE EJEMPLO ===\n")

    # Crear segundo Pikachu
    pikachu2 = Pikachu("Thunder", 7, 120, 1200, 60, "amarillo brillante")

    # Batalla
    pikachu.atacar(pikachu2)
    print()
    pikachu2.impactrueno(pikachu)
    print()

    # Mostrar estados usando getters indirectamente (método mostrar_estado los
    # usa)
    pikachu.mostrar_estado()
    pikachu2.mostrar_estado()
