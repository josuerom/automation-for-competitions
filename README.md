# Automatizaciones en Generación Rápida de Archivos para Concursos de PC

Este es un repositorio personal con soluciones, plantillas y utilidades para la PC enfocados a los tres únicos mejores lenguajes en el deporte **C++**, **Java** y **Python**.

---

## 📘 ¿Qué encontrarás aquí?

- Soluciones a problemas de plataformas como Codeforces y RPC Colombia.
- Plantillas listas para usar con entrada/salida rápida.
- Archivos organizados por lenguaje.
- Ejemplos de código limpios, funcionales y reutilizables.

---

## 🎯 ¿Para quién es este repositorio?

- Estudiantes que practican programación competitiva.
- Participantes de maratones o concursos (ICPC, CODEFORCES, VJUDGE, UVA, etc.).
- Programadores que buscan plantillas rápidas para solucionar problemas.

---

## 📂 Estructura del proyecto

```
/
├── util/       # Almacenamiento de herramientas y utilidades
├── contests/   # Almacenamiento de participaciones de concursos en línea
└── README.md   # Documentación del proyecto
```

---

## 🛠️ Requisitos

Necesitas tener instalado:

- **Python**: versión >= 3.7
- **Git** (opcional):

```bash
git clone https://github.com/josuerom/automation-for-competitions.git
cd automation-for-competitions
```

---

## ▶️ Cómo ejecutar una solución

### 🟦 C++

```bash
cd cpp/
g++ -std=c++20 -O2 nombre.cpp -o programa
./programa < input.txt > output.txt
```

### ☕ Java

```bash
cd java/
javac Nombre.java
java Nombre < input.txt > output.txt
```

### 🐍 Python

```bash
cd python/
python3 -OO nombre.py < input.txt > output.txt
```

---

## ✍️ Cómo añadir tus propias soluciones

1. Entra al directorio del lenguaje (`cpp/`, `java/`, `python/`)
2. Copia un archivo base desde `templates/`
3. Renómbralo con el nombre del problema
4. Escribe tu solución, pruébala y guarda los cambios
5. ¡Listo para hacer commit y subir!

**NOTA**: le recomiendo convertir los programas en `.exe` con el fin de invocarlos desde cualquier parte de su sistema, incluyendolos a las variables de entorno `Path`.

---

## 📄 Ejemplo de plantilla en C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
   ios::sync_with_stdio(false);
   cin.tie(nullptr);
   int tt;
   cin >> tt;
   while (tt--) {
       // algoritmo
   }
   return 0;
}
```

---

## 🤝 Contribuciones

Si deseas aportar:

- Mejora las plantillas
- Sube soluciones a nuevos problemas
- Arregla errores o ayuda con documentación

Haz un fork, crea una rama y envía un Pull Request. Toda mejora es bienvenida 🚀

---

## 📜 Licencia

Este repositorio está bajo la licencia personalizada. Debe leerla ahora.

---

## 📫 Contacto

¿Tienes sugerencias o ideas?

Puedes abrir un issue en el repositorio.

---

**¡Gracias por haber leido, espero que uses las automatizaciones! (hágale que no viene carro)** 🧠💻
