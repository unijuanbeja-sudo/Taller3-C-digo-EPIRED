# ==========================================================
# EPIRED COLOMBIA
# BST de reportes epidemiológicos con menú
# ==========================================================


class NodoReporte:
    def __init__(
        self,
        codigo,
        enfermedad,
        fecha,
        estado,
        municipio,
        centroSalud
    ):
        self.codigo = codigo
        self.enfermedad = enfermedad
        self.fecha = fecha
        self.estado = estado
        self.municipio = municipio
        self.centroSalud = centroSalud

        self.izquierdo = None
        self.derecho = None

    def mostrar(self):
        print("\n--- DATOS DEL REPORTE ---")
        print("Código:", self.codigo)
        print("Enfermedad:", self.enfermedad)
        print("Fecha:", self.fecha)
        print("Estado:", self.estado)
        print("Municipio:", self.municipio)
        print("Centro de salud:", self.centroSalud)


class ArbolReportesBST:
    def __init__(self):
        self.raiz = None

    # Convierte REP-2026-050 en 50
    def obtener_clave(self, codigo):
        return int(codigo.split("-")[-1])

    # ------------------------------------------------------
    # INSERTAR
    # ------------------------------------------------------
    def insertar(self, reporte):
        if self.raiz is None:
            self.raiz = reporte
            return True

        clave_nueva = self.obtener_clave(reporte.codigo)
        actual = self.raiz

        while True:
            clave_actual = self.obtener_clave(actual.codigo)

            if clave_nueva == clave_actual:
                print("\nYa existe un reporte con esa clave.")
                return False

            if clave_nueva < clave_actual:
                if actual.izquierdo is None:
                    actual.izquierdo = reporte
                    return True

                actual = actual.izquierdo

            else:
                if actual.derecho is None:
                    actual.derecho = reporte
                    return True

                actual = actual.derecho

    # ------------------------------------------------------
    # BUSCAR
    # ------------------------------------------------------
    def buscar(self, codigo):
        clave_buscada = self.obtener_clave(codigo)
        actual = self.raiz

        while actual is not None:
            clave_actual = self.obtener_clave(actual.codigo)

            if clave_buscada == clave_actual:
                return actual

            if clave_buscada < clave_actual:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    # ------------------------------------------------------
    # ELIMINAR
    # ------------------------------------------------------
    def eliminar(self, codigo):
        if self.buscar(codigo) is None:
            return False

        clave = self.obtener_clave(codigo)
        self.raiz = self._eliminar_recursivo(self.raiz, clave)
        return True

    def _eliminar_recursivo(self, nodo, clave):
        if nodo is None:
            return None

        clave_nodo = self.obtener_clave(nodo.codigo)

        if clave < clave_nodo:
            nodo.izquierdo = self._eliminar_recursivo(
                nodo.izquierdo,
                clave
            )

        elif clave > clave_nodo:
            nodo.derecho = self._eliminar_recursivo(
                nodo.derecho,
                clave
            )

        else:
            # Caso 1: nodo hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            # Caso 2: solamente tiene hijo derecho
            if nodo.izquierdo is None:
                return nodo.derecho

            # Caso 2: solamente tiene hijo izquierdo
            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: tiene dos hijos
            sucesor = self._obtener_minimo(nodo.derecho)

            nodo.codigo = sucesor.codigo
            nodo.enfermedad = sucesor.enfermedad
            nodo.fecha = sucesor.fecha
            nodo.estado = sucesor.estado
            nodo.municipio = sucesor.municipio
            nodo.centroSalud = sucesor.centroSalud

            clave_sucesor = self.obtener_clave(sucesor.codigo)

            nodo.derecho = self._eliminar_recursivo(
                nodo.derecho,
                clave_sucesor
            )

        return nodo

    def _obtener_minimo(self, nodo):
        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    # ------------------------------------------------------
    # IN-ORDER: izquierda, raíz, derecha
    # ------------------------------------------------------
    def mostrar_inorder(self):
        print("\nRECORRIDO IN-ORDER:")
        self._inorder(self.raiz)
        print()

    def _inorder(self, nodo):
        if nodo is not None:
            self._inorder(nodo.izquierdo)
            print(nodo.codigo, end="  ")
            self._inorder(nodo.derecho)

    # ------------------------------------------------------
    # PRE-ORDER: raíz, izquierda, derecha
    # ------------------------------------------------------
    def mostrar_preorder(self):
        print("\nRECORRIDO PRE-ORDER:")
        self._preorder(self.raiz)
        print()

    def _preorder(self, nodo):
        if nodo is not None:
            print(nodo.codigo, end="  ")
            self._preorder(nodo.izquierdo)
            self._preorder(nodo.derecho)


# ==========================================================
# CREACIÓN DEL ÁRBOL INICIAL
# ==========================================================

arbol = ArbolReportesBST()

reportes_iniciales = [
    NodoReporte(
        "REP-2026-050",
        "Dengue",
        "2026-08-12",
        "Confirmado",
        "Bogotá",
        "Hospital Central"
    ),
    NodoReporte(
        "REP-2026-030",
        "Malaria",
        "2026-08-08",
        "En estudio",
        "Quibdó",
        "Hospital San Francisco"
    ),
    NodoReporte(
        "REP-2026-070",
        "Influenza",
        "2026-08-15",
        "Recuperado",
        "Medellín",
        "Clínica Norte"
    ),
    NodoReporte(
        "REP-2026-020",
        "Zika",
        "2026-08-04",
        "Descartado",
        "Cali",
        "Hospital Universitario"
    ),
    NodoReporte(
        "REP-2026-040",
        "Chikungunya",
        "2026-08-10",
        "Confirmado",
        "Neiva",
        "Clínica del Huila"
    ),
    NodoReporte(
        "REP-2026-060",
        "Leptospirosis",
        "2026-08-14",
        "En estudio",
        "Barranquilla",
        "Hospital del Caribe"
    ),
    NodoReporte(
        "REP-2026-080",
        "Sarampión",
        "2026-08-18",
        "Confirmado",
        "Bucaramanga",
        "Hospital Metropolitano"
    )
]

for reporte in reportes_iniciales:
    arbol.insertar(reporte)


# ==========================================================
# MENÚ DEL PROGRAMA
# ==========================================================

def mostrar_menu():
    print("\n" + "=" * 55)
    print("       EPIRED COLOMBIA - ÁRBOL BST")
    print("=" * 55)
    print("1. Insertar reporte")
    print("2. Buscar reporte")
    print("3. Eliminar reporte")
    print("4. Mostrar recorrido In-Order")
    print("5. Mostrar recorrido Pre-Order")
    print("0. Salir")
    print("=" * 55)


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    # INSERTAR
    if opcion == "1":
        print("\n--- INSERTAR REPORTE ---")

        codigo = input("Código (ejemplo REP-2026-065): ")
        enfermedad = input("Enfermedad: ")
        fecha = input("Fecha: ")
        estado = input("Estado: ")
        municipio = input("Municipio: ")
        centroSalud = input("Centro de salud: ")

        try:
            nuevo_reporte = NodoReporte(
                codigo,
                enfermedad,
                fecha,
                estado,
                municipio,
                centroSalud
            )

            if arbol.insertar(nuevo_reporte):
                print("\nReporte insertado correctamente.")

        except ValueError:
            print("\nEl código debe terminar en un número.")

    # BUSCAR
    elif opcion == "2":
        print("\n--- BUSCAR REPORTE ---")

        codigo = input("Ingrese el código: ")

        try:
            reporte_encontrado = arbol.buscar(codigo)

            if reporte_encontrado is not None:
                print("\nReporte encontrado.")
                reporte_encontrado.mostrar()
            else:
                print("\nEl reporte no existe.")

        except ValueError:
            print("\nEl código debe terminar en un número.")

    # ELIMINAR
    elif opcion == "3":
        print("\n--- ELIMINAR REPORTE ---")

        codigo = input("Ingrese el código: ")

        try:
            if arbol.eliminar(codigo):
                print("\nReporte eliminado correctamente.")
            else:
                print("\nEl reporte no existe.")

        except ValueError:
            print("\nEl código debe terminar en un número.")

    # IN-ORDER
    elif opcion == "4":
        arbol.mostrar_inorder()

    # PRE-ORDER
    elif opcion == "5":
        arbol.mostrar_preorder()

    # SALIR
    elif opcion == "0":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción no válida. Intente nuevamente.")

    input("\nPresione Enter para continuar...")
