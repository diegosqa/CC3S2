# Informe de Configuración de CI/CD con Docker y GitHub Actions

## Introducción

Este informe detalla el proceso que se ha seguido para realizar la Actividad 1

## Ubicación del proyecto desarrollado

- **GitHub**: https://github.com/diegosqa/devops-practice


## Desarrollo

### Iniciando el proyecto
Antes de iniciar con el proyecto vamos a proceder a crear el la carpeta *devops-practice* e instalaremos todas las dependencias que vamos a necesitar

![Instalando dependecias](Imagenes/Foto1.PNG)

Procedemos a crear las carpetas necesarias para nuestra aplicación *usaremos el editor VI para esto*

![Instalando dependecias](Imagenes/Foto2.PNG)

Creamos la clase *tests/app.test.js*

![Instalando dependecias](Imagenes/Foto3.PNG)

Creamos la clase *src/app.js*

![Instalando dependecias](Imagenes/foto22.PNG)

Editamos el archivo *package.json*

![Instalando dependecias](Imagenes/Foto4.PNG)

### Editando el archivo para hacer CI/CD

Ahora vamos a iniciar con la parte mas importante de esta actividad que es crear el pipeline
Procederemos a crear un archivo *.github/workflows/ci.yml*

![Instalando dependecias](Imagenes/Foto5.PNG)

Vamos añadirle lo siguiente

![Instalando dependecias](Imagenes/foto23.PNG)

CI Pipeline - Descripción

Este workflow de GitHub Actions automatiza pruebas para un proyecto Node.js.

Configuración

- **Evento**: Se ejecuta en `push` y `pull_request` en `main`.
- **Entorno**: `ubuntu-latest`.

Pasos

1. **Clonar repositorio**: `actions/checkout@v2`.
2. **Configurar Node.js (v14)**: `actions/setup-node@v2`.
3. **Instalar dependencias**: `npm install`.
4. **Ejecutar pruebas**: `npm test`.

Automatiza pruebas en cada cambio en `main`.

Luego de esto vamos a iniciar un proyecto en git ( antes de eso ya creamos nuestro repositorio en github llamado devops-practice)

![Instalando dependecias](Imagenes/Foto6.PNG)
![Instalando dependecias](Imagenes/Foto7.PNG)

Luego vamos a revisar en nuestro repo Actions para ver que todo haya salido bien

![Instalando dependecias](Imagenes/Foto8.PNG)

![Instalando dependecias](Imagenes/Foto9.PNG)

Dado que nuestro codigo se ha lanzado con un bucle ( ya que nunca se cerraba el servidor por lo que lograba terminar todo, pero los test si funcionaban)

![Instalando dependecias](Imagenes/foto24.PNG)

Entonces se procedio a cambiar las clases para lograr un mejor resultado ( nos guiamos del repositorio del profesor para lograr esto)

Cambiamos las clases de la siguiente manera para obtener un mejor resultado

Clase *app.js*

![Instalando dependecias](Imagenes/Foto25.PNG)

Clase *app.test.js*

![Instalando dependecias](Imagenes/Foto26.PNG)

Con esto hacemos un push a nuestra rama main y vemos que obtenemos mejores resultados

![Instalando dependecias](Imagenes/Foto15.PNG)

Revisamos nuestro pipeline

![Instalando dependecias](Imagenes/Foto14.PNG)

### Docker 

Vamos a proceder a crear nuestro archivo Docker

![Instalando dependecias](Imagenes/Foto10.PNG)

Editamos el siguiente archivo con lo siguiente

![Instalando dependecias](Imagenes/Foto11.PNG)

Asimismo, vamos a editar el archivo ci.yml ya que tenemos nuevos procesos que examinar

![Instalando dependecias](Imagenes/Foto27.PNG)
![Instalando dependecias](Imagenes/Foto28.PNG)

Y con todo esto, vamos a proceder a construir nuestra imagen

![Instalando dependecias](Imagenes/Foto18.PNG)

Hacemos un push a la main para correr el proceso y nos sale el siguiente mensaje

![Instalando dependecias](Imagenes/Foto29.PNG)

Y esto se debe a que pusimos *ame* y no name en nuestro archivo ci.yml

![Instalando dependecias](Imagenes/Foto30.PNG)

Arreglamos ese error, volvemos a hacer un push y vemos que todo esta muy bien

![Instalando dependecias](Imagenes/Foto31.PNG)


