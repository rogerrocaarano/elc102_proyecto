# Proyecto de Programación gráfica

## Ventana principal

Menú Lienzo:

- Limpiar lienzo
- Cambiar color del lienzo
- Cambiar color del pincel

Menú Dibujar:

- Línea
- Cuadrado
- Rectángulo
- Triángulo
- Polígono

Menú 3D Viewer:

- Abrir archivo: Despliega un cuadro de diálogo para seleccionar un archivo Wayform con extensión .obj.

Las dos últimas figuras que se dibujen en el lienzo pueden ser movidas con las flechas del teclado y 
las teclas W, A, S, D.

Si se detecta que las figuras colisionan, se muestra un modal con el mensaje de colisión.

Los dibujos se realizan en tiempo real, para mejorar la experiencia del usuario.

Cada figura puede tener un color distinto, el color se guarda en el objeto de la figura al momento de
dibujarla.

# Ventana de visualización 3D

Al abrir un objeto desde el menú 3D Viewer, se abre una nueva ventana con el objeto cargado.

La ventana de visualización 3D cuenta con un menú para cambiar la posición de la cámara desde la 
cual se está visualizando.

Se utilizó OpenGL para la visualización 3D y la iluminación de la escena.


# Entorno de desarrollo

Se utilizó Pycharm como IDE.

Se eligió como lenguaje de programación Python, en la versión 3.11 y como librería gráfica PySide6
en su versión 6.2.0 y PyOpenGL en su versión 3.1.5.

Crear un ambiente virtual de python, activarlo y ejecutar el siguiente comando para instalar las dependencias:

```
pip install -r requirements.txt
```
Para crear un ejecutable, ejecutar el siguiente comando:

```
pyinstaller -n elc102_proyecto  -w main.py
```
