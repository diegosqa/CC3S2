# Practicando Github

## Introducción

Este informe detalla el proceso que se ha seguido para realizar la Actividad 3



## Desarrollo

### Ejercicio 1
Iniciamos el repo, cambiamos el nombre de la rama main a main, creamos el archivo main.py y lo editamos

![Instalando dependecias](Imagenes/Foto1.PNG)

Agregamos lo siguiente al archivo

![Instalando dependecias](Imagenes/Foto2.PNG)


Luego vamos añadir estos cambios a la rama main, commiteamos y lo dejamos en el stage, luego procedemos a crear una nueva rama donde vamos a dirigirnos para editar el main.py

![Instalando dependecias](Imagenes/foto3.PNG)

Editamos el main.py en la rama feature/advanced-feature

![Instalando dependecias](Imagenes/Foto4.PNG)

De igual manera añadimos esto a la rama, y commiteamos para dejarlo en el stage

![Instalando dependecias](Imagenes/Foto5.PNG)

Cambiamos a la rama main para editar el archivo main.py, ya que queremos crear un conflicto 

![Instalando dependecias](Imagenes/foto6.PNG)


Lo editamos de la siguiente manera


![Instalando dependecias](Imagenes/Foto7.PNG)

Añadimos estos cambios a la rama main.py, y commiteamos
Luego verificamos que ocurre un error ya que hay conflicto entre ambas ramas

![Instalando dependecias](Imagenes/Foto8.PNG)

Al revisar el archivo verificamos lo siguiente

![Instalando dependecias](Imagenes/Foto9.PNG)

Editamos el archivo para que no cause un conflicto, una de las soluciones es lo siguiente

![Instalando dependecias](Imagenes/foto10.PNG)

Como nos damos cuenta, estamos en la rama main | merging, por lo que debemos añadir este cambio para poder resolver el conflicto. Luego de hacer commit verificamos que efectivamente se pudo realziar el merge

![Instalando dependecias](Imagenes/Foto11.PNG)

Ahora haremos el comando git -log

![Instalando dependecias](Imagenes/Foto12.PNG)
A continuación un breve resumen de lo que se realizo

**commit 718616ffb39e1b34c0507ce797214d12d079bef**
Se resolvió el conflicto al intentar hacer el merge entre la rama main y la rama feature/advanced-feature.
    El archivo resultante contiene ambos mensajes: "Hello World - updated in main" y "Hello from advanced feature".
**commit c7199d34bcae2e8cd1b79a627e3330660246e27c**
En este commit, se actualizó el mensaje del archivo main.py en la rama main.
    El mensaje se cambió de "Hello from initial main" a "Hello World - updated in main".
**commit cc66743b564dfc7778c0c806d8bc194f3affaab**
En este commit, se modificó el archivo main.py en la rama feature/advanced-feature.
    El mensaje original fue cambiado de "Hello from initial main" a "Hello from advanced feature".
**commit 591797610f1876db9c921685706ce3b86f0f29cb**
En este commit inicial, se creó el archivo main.py con el mensaje "Hello from initial main".

Ahora hacemos el *git log --author="Diego Quispe"* para ver mis commits
![Instalando dependecias](Imagenes/Foto13.PNG)

### Ejercicio 2
Antes de hacer un *revert* vamos a editar el archivo main.py
![Instalando dependecias](Imagenes/Foto14.PNG)
Luego de añadirlo con el git add y commit, vamos a ver el status para ver que no hay nada pendiente, luego de eso veremos el git log --online para observar el ultimo commit que se hizo y como esta el HEAD. Como vemos se hizo posible el git revert HEAD
y aparece como Revert. 
![Instalando dependecias](Imagenes/Foto15.PNG)
Luego de eso vamos hacer un rebaste, editamos el archivo para que todo apunte el cc66743
![Instalando dependecias](Imagenes/Foto17.PNG)
Aca vemos como tuve algunos problemas de conflictos, pero se pudo resolver 
![Instalando dependecias](Imagenes/Foto18.PNG)
Finalmente vemos que si se pudo juntar todo y apuntando al que queriamos que en este caso es el commit de Add greet function in advanced feature
![Instalando dependecias](Imagenes/Foto19.PNG)
Aca verificamos que tenemos ya todo mas ordenado y la ventaja es que podemos eliminar algunos commits luego de hacer un gran cambio, para poder trabajar de manera correcta.
![Instalando dependecias](Imagenes/Foto20.PNG)
### Ejercicio 3
Vamos hacer a crear una rama *bugfix/rollback-feature* a partir de nuestro primer commit
![Instalando dependecias](Imagenes/Foto21.PNG)
Vamos a editar el main.py en la nueva rama con lo siguiente:
![Instalando dependecias](Imagenes/Foto22.PNG)
Luego de eso agregamos haciendo un add. , luego un commit para posterior a eso cambiar a la rama main y hacer un merge. Como vemos hay conflicto, entonces procedemos a editar el main
![Instalando dependecias](Imagenes/Foto23.PNG)
Editamos el archivo de la siguiente manera
![Instalando dependecias](Imagenes/Foto24.PNG)
Finalmente resolvemos el conflicto y vemos como se encuentra nuestro repositorio con respecto a los logs, ahi podemos ver un poco mas del historial
![Instalando dependecias](Imagenes/Foto25.PNG)
Finalmente eliminamos la rama que hemos creado
![Instalando dependecias](Imagenes/Foto26.PNG)

### Ejercicio 4
En este caso vamos a editar nuestro main con lo siguiente
![Instalando dependecias](Imagenes/Foto27.PNG)
Agregamos estos cambios para tenerlos en el HEAD, luego de eso hacer un --hard HEAD-1 para volver al anterior y deshacer lo que hicimos
![Instalando dependecias](Imagenes/Foto28.PNG)
Al visualizar nuevamente vemos que no se origino ningún cambio y volvio al estado anterior
![Instalando dependecias](Imagenes/Foto29.PNG)
Otra manera de hacer esto ( esto son para los cambios que solo esta en un add., si ya han sido commiteados lo mejor es usar lo que esta arriba)
Vemos que el status es que ha sido modificado el main.py, entonces para deshacer esto solo hacemos un restore para omitir todos los cambios que estan en el stage
![Instalando dependecias](Imagenes/Foto30.PNG)
Como vemos volvio a la normalidad si ningún cambio
![Instalando dependecias](Imagenes/Foto31.PNG)


### Ejercicio 5
![Instalando dependecias](Imagenes/Foto32.PNG)
![Instalando dependecias](Imagenes/Foto33.PNG)
![Instalando dependecias](Imagenes/Foto34.PNG)
![Instalando dependecias](Imagenes/Foto35.PNG)
![Instalando dependecias](Imagenes/Foto36.PNG)
![Instalando dependecias](Imagenes/Foto37.PNG)
![Instalando dependecias](Imagenes/Prueba38.PNG)
![Instalando dependecias](Imagenes/Foto39.PNG)
### Ejercicio 6
![Instalando dependecias](Imagenes/Foto40.PNG)


