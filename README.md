<h1 align="center">
<br>
  <img src="https://images.squarespace-cdn.com/content/v1/56c240a0d51cd440f4c3f6ca/1605347300629-TR8LONJMS1YM7ZA6KNYA/circulo-de-quintas.jpg" alt="MVC" width="386" height="384">
<br>
<br>
Generador de Escalas Mayores y Acordes Diatónicos
</h1>

<hr />
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->


## Description
Pequeño programa en python que genera las 12 escalas mayores y sus respectivos acordes siguiendo el patron del ciruclo de quintas. 

## Info

 - Version de python - 3.8.5

## Interfaz de usuario

```
¡¡Bienvenido al generador de escalas MAYORES!!
Para generar tu escala MAYOR debes ingresar el nombre de una nota cualquiera en notación americana (C,D,E,F,G,A,B) --> (DO,RE,MI,FA,SOL,LA,SI)
Puedes agregar bemoles y sostenidos siguiendo el patrón de generación de escalas mayores dictado por el circulo de quintas. 
------------------------------------------------------------------------------------------ 
Lista de las 12 escalas mayores: 'C','C#','D','D#','E','F','F#','G','G#','A','A#','B'  
Posibles combinaciones de acordes: 'D','Dm','D#m','Dbm'... para el acorde de RE o D. 
------------------------------------------------------------------------------------------ 
NOTA: VII° --> Quiere decir septimo acorde de la escala y es disminuido. Ej. C = C, E, G --> Cm(dim) = C, Eb, Gb

Ante las dudas... prueba, prueba y prueba! ...¡COMENZEMOS!


Seleccione una opción. (Sostenidos = '#', Bemoles = 'b')
        1. Generar escala mayor a partir de nota base
        2. Mostrar triada a partir de especificació acorde
        3. Generar escala y acordes a partir de nota base 
        4. Adios musical
```

### Opcion 1
```
Ingrese una opcion: 1
Ingrese el nombre de la nota para obtener una escala: C
__________________Escala de C_________________
-----------------------------------------------
I   : C
II  : Dm
III : Em
IV  : F
V   : G
VI  : Am
VII°: Bm
_______________________________________________
-----------------------------------------------
```

### Opcion 2
```
Ingrese una opcion: 2
Ingrese el acorde para obtener sus forma de triada: D
['D', 'F#', 'A']

...

Ingrese el acorde para obtener sus forma de triada: Dm
['D', 'F', 'A']

Ingrese el acorde para obtener sus forma de triada: D#
['D#', 'G', 'A#']

Ingrese el acorde para obtener sus forma de triada: D#m
['D#', 'F#', 'A#']
```

### Opcion 3
```
Ingrese una opcion: 3
Ingrese el nombre de la nota para obtener una escala y sus acordes: C
__________________Escala de C_________________
-----------------------------------------------
I   : C - ['C', 'E', 'G']
II  : Dm - ['D', 'F', 'A']
III : Em - ['E', 'G', 'B']
IV  : F - ['F', 'A', 'C']
V   : G - ['G', 'B', 'D']
VI  : Am - ['A', 'C', 'E']
VII°: Bm - ['B', 'D', 'Gb']
_______________________________________________
-----------------------------------------------
```

## References
 - El Circulo de Quintas: una explicacion detallada - https://www.youtube.com/watch?v=r0R6gMw2s44 

## License
No license.
