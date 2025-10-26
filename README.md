# preentregaluzfox
Preentrega del Proyecto de QA Automation de Talent Tech

# Pre-entrega Proyecto Final - Automatización de Testing

Este proyecto implementa una automatización de pruebas para el sitio **SauceDemo**, utilizando **Selenium WebDriver** y **Python**.

## 🎯 Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Pytest**: Framework de testing para estructurar y ejecutar pruebas
- **Selenium WebDriver**: Para la automatización de la interfaz web
- **Git/GitHub**: Para control de versiones y compartir el código

## 📁 Estructura del Proyecto

PreentregaLuzFox/ 
├── test/ 
│     ├── test_login.py         # Pruebas relacionadas con el Login. 
│     ├── test_inventory.py     # Pruebas de Inventario y Elementos. 
│     └── test_cart.py          # Pruebas de Carrito y Flujo de Productos.
│ 
├── utils.py                # Funciones Login (Inicialización de Chrome/Driver). 
├── conftest.py             # Hooks de Pytest, fixtures. 
├── report.html             # Reporte final generado por pytest. 
├── README.md               # Describe las funcionalidades del programa. 
├── run_tests.py            # Archivo main para la ejecución de los tests. 



## ⚙️ Instalación de Dependencias

1. Asegúrate de tener Python 3.7 o superior instalado.
2. Instala las dependencias necesarias:

pip install selenium pytest pytest-html

Descarga el WebDriver correspondiente a tu navegador:

ChromeDriver

Asegúrate de que el WebDriver esté en tu PATH o especifica su ubicación en el código.

▶️ Ejecución de las Pruebas
Para ejecutar todas las pruebas:
py -m pytest Preentrega-LuzFox/run_tests.py

Para generar un reporte HTML:
py -m pytest Preentrega-LuzFox/run_tests.py
El reporte se ejecuta conjuntamente en run_tests.py 

✅ Funcionalidades Implementadas

1. Automatización de Login
   Caso de éxito con credenciales válidas

Caso de fallo con credenciales inválidas

2. Verificación del Catálogo
   Comprobación del título de la página

Verificación de presencia de productos

3. Interacción con el Carrito
   Añadir producto al carrito

Verificar que el contador se incremente

Navegar al carrito

Comprobar que el producto añadido aparezca correctamente

4. Cierre de Sesión
   Verificar que el usuario pueda cerrar sesión correctamente

✨ Características Adicionales

Funciones auxiliares reutilizables: En el archivo utils.py.

👤 Autor
[Luz Fox]

📝 Notas
Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing.
Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.

