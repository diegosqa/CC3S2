# Informe de Configuración de CI/CD con Docker y GitHub Actions

## Introducción

Este informe detalla el proceso que se ha seguido para realizar la Actividad 2

## Ubicación del proyecto desarrollado

- **GitHub**: https://github.com/diegosqa/devops_practice


## Desarrollo

### Iniciando el proyecto
Antes de iniciar con el proyecto vamos a proceder a crear el la carpeta *devops-practice* e instalaremos todas las dependencias que vamos a necesitar

![Instalando dependecias](Imagenes/Foto1.PNG)

Procedemos a crear todo lo necesario para iniciar nuestro proyecto como las carpetas y el npm init-y

![Instalando dependecias](Imagenes/Foto2.PNG)


Creamos la clase *src/test.app.js*

![Instalando dependecias](Imagenes/foto3.PNG)

Editamos el archivo *package.json*

![Instalando dependecias](Imagenes/Foto4.PNG)

### Realizando las verificaciones para que corran las pruebas

Antes iniciar con lo que sigue del proyecto vamos a continuar ejecutando *npm test* para verificar que las pruebas se esten ejecutando con exito

![Instalando dependecias](Imagenes/Foto5.PNG)

Asimismo vamos a correr el npm *audit* para verificar que no hay ningún problema de seguridad 

![Instalando dependecias](Imagenes/foto6.PNG)

### CI Pipeline - Descripción

Este workflow de GitHub Actions automatiza pruebas para un proyecto Node.js.


Luego de esto vamos a editar el workflow para validar que se ejecute correctamente el pipeline, en el cual van a correr tanto los test como la auditoria


![Instalando dependecias](Imagenes/Foto7.PNG)

Luego vamos a crear nuestra imagen de docker antes de construir nuestro contenedor

![Instalando dependecias](Imagenes/Foto9.PNG)

Posteriormente vamos a crear nuestro contenedor para que todo salga bien 

![Instalando dependecias](Imagenes/Foto8.PNG)

En este punto vamos a lanzar correr el contenedor para validar que realmente este escuchando por el puerto 3000

![Instalando dependecias](Imagenes/foto10.PNG)

Entonces procedemos a validar que realmente se pueda mostrar el Hello World en nuestro navegador

![Instalando dependecias](Imagenes/Foto11.PNG)

En este punto vamos a crear nuestro *docker-compose.yml* orquestar todo

![Instalando dependecias](Imagenes/Foto12.PNG)

Editamos nuestro *docker-compose.yml*

![Instalando dependecias](Imagenes/Foto13.PNG)

Corremos nuestro docker compose

![Instalando dependecias](Imagenes/Foto14.PNG)

### Observabilidad

Crearemos nuestro *prometheus.yml*

![Instalando dependecias](Imagenes/Foto15.PNG)

Actualizamos nuestro docker compose para incluir grafana

![Instalando dependecias](Imagenes/Foto16.PNG)

Verificamos que todo este bien, verificamos en el puerto 9090 que prometheus este corriendo

![Instalando dependecias](Imagenes/Foto17.PNG)


Asimismo verificamos en el puerto 3001 que se encuentre corriendo grafana para ver las métricas

![Instalando dependecias](Imagenes/Foto18.PNG)

Hacemos un push a la main para correr el proceso y nos sale el siguiente mensaje

![Instalando dependecias](Imagenes/Foto19.PNG)




