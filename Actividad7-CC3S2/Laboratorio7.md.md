
# Ejercicios de Git
Alumnos: Diego Sebastian Quispe Amao
Codigo: 20202222I

Este es la resolución del laboratorio numero 7

## Ejercicio 1: git checkout --ours y git checkout --theirs

**Pregunta**: ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto?

**Respuesta**:
- Si usas `git checkout --ours`, estarías priorizando los cambios que tú o tu equipo hicieron, básicamente diciendo "prefiero mis cambios". Por otro lado, `git checkout --theirs` elige los cambios de la otra rama, o sea, los del equipo B.
- ¿Cuándo usar uno u otro? Pues depende de quién tenga la razón o los mejores cambios en el contexto del conflicto.
- Después de resolver el conflicto, siempre ejecuta tus pruebas para asegurarte de que todo siga funcionando bien. Esto es importante para no detener la pipeline de CI/CD por un error.

---

## Ejercicio 2: git diff

**Pregunta**: ¿Cómo usarías `git diff` para comparar los cambios entre ramas y detectar conflictos?

**Respuesta**:
- Para esto, el comando `git diff feature-branch..main` es súper útil. Te muestra exactamente qué cosas son diferentes entre las dos ramas. Entonces, antes de hacer una fusión, revisas bien con este comando y te ahorras futuros dolores de cabeza.
- Con esto puedes ver si algo en los archivos críticos va a causar conflictos antes de fusionar, así que ayuda bastante a evitar problemas en la CI/CD y mantiene todo estable.

---

## Ejercicio 3: git merge --no-commit --no-ff

**Pregunta**: ¿Cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión?

**Respuesta**:
- Básicamente, `git merge --no-commit --no-ff` te permite ver cómo quedaría la fusión de dos ramas, pero sin hacer ningún commit. Esto es como una "prueba", para ver si va a funcionar o no.
- La ventaja es que puedes identificar posibles errores o conflictos antes de hacer la fusión final. Así te aseguras de que todo esté bien antes de comprometer los cambios en el historial.
- En una pipeline de CI/CD podrías automatizar este paso para revisar siempre las fusiones antes de que sean definitivas.

---

## Ejercicio 4: git mergetool

**Pregunta**: ¿Cómo configurarías y utilizarías `git mergetool` en tu equipo?

**Respuesta**:
- `git mergetool` es genial si prefieres usar una herramienta gráfica para resolver conflictos. Puedes configurar herramientas como `vimdiff` o VS Code con este comando y facilita mucho la vida.
- En equipos ágiles, usar una herramienta visual para resolver conflictos puede acelerar bastante el proceso y reducir errores, sobre todo si todos están en la misma página usando la misma herramienta.

---

## Ejercicio 5: git reset

**Pregunta**: ¿Cuál es la diferencia entre `git reset --soft`, `git reset --mixed`, y `git reset --hard`? Describe un caso donde usarías `git reset --mixed`.

**Respuesta**:
- **`git reset --soft`**: Solo mueve el puntero del commit, pero los archivos y el índice siguen igual.
- **`git reset --mixed`**: Resetea el índice, pero deja tus archivos modificados sin tocar.
- **`git reset --hard`**: Lo borra todo, como si nunca hubieras hecho esos cambios.
  
Caso práctico: Si haces un commit que rompe la pipeline de CI/CD y necesitas corregirlo pero no perder el trabajo, `git reset --mixed` es lo mejor. Puedes corregir lo que hiciste mal sin borrar lo que ya tenías.

---

## Ejercicio 6: git revert

**Pregunta**: ¿Cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial?

**Respuesta**:
- Si necesitas deshacer algo pero no puedes cambiar el historial, `git revert` es tu amigo. Crea un commit nuevo que "deshace" los cambios de otro commit.
- Un ejemplo sería si hiciste dos commits con errores, podrías usar `git revert <hash1> <hash2>` para revertir ambos sin tocar el historial, lo que mantendría la estabilidad en tu pipeline de CI/CD.

---

## Ejercicio 7: git stash

**Pregunta**: ¿Cómo usarías `git stash` para guardar temporalmente tus cambios?

**Respuesta**:
- `git stash` es ideal cuando tienes trabajo pendiente pero necesitas cambiar de rama rápidamente. Guardas todo lo que has hecho y puedes retomarlo después.
  ```bash
  git stash
  git checkout hotfix-branch
  ```
- Luego, cuando termines con la rama de hotfix, puedes recuperar tus cambios:
  ```bash
  git stash apply
  ```
- Esto es útil en un flujo de trabajo ágil donde tienes que trabajar en múltiples tareas al mismo tiempo sin perder tu progreso.

---

## Ejercicio 8: .gitignore

**Pregunta**: Diseña un archivo `.gitignore` para un entorno de desarrollo ágil.

**Respuesta**:
```gitignore
# Archivos de entorno
*.env
# Archivos de configuración personal
*.config
# Archivos de logs
logs/
*.log
# Dependencias locales
node_modules/
vendor/
```
- Mantener este archivo `.gitignore` actualizado es importante porque asegura que solo los archivos relevantes lleguen al repositorio, evitando problemas en la CI/CD y asegurando que el código compartido esté limpio.

---

## Ejercicio 1: Resolución de conflictos en un entorno ágil

**Pregunta**: ¿Cómo gestionarías la resolución de conflictos de manera eficiente utilizando Git?

**Respuesta**:
- Lo primero sería identificar el conflicto con `git diff` y decidir cómo resolverlo. Usaría `git mergetool` para resolver los conflictos visualmente.
- Luego, verificaría que la solución no cause problemas corriendo todas las pruebas locales y CI/CD antes de hacer el commit final.
- Finalmente, hago el commit y continúo con la entrega continua.

---

## Ejercicio 2: Rebase vs Merge en integraciones ágiles

**Pregunta**: ¿Cuáles son las ventajas y desventajas de `rebase` y `merge` en integraciones ágiles?

**Respuesta**:
- **Merge**: Mantiene todo el historial de commits, lo que es bueno para saber cómo llegaron los cambios. Pero, puede hacer que el historial sea un poco confuso.
- **Rebase**: Hace que el historial sea más limpio y fácil de seguir, pero puede ser problemático si lo usas en ramas compartidas.
  
En CI/CD, `merge` puede generar más conflictos de revisión, mientras que `rebase` ayuda a mantener un historial más fácil de revisar y encontrar errores.

---

## Ejercicio 3: Git Hooks en CI/CD ágil

**Pregunta**: ¿Cómo diseñarías un conjunto de Git Hooks para mitigar problemas de código?

**Respuesta**:
- **Pre-commit hook**: Aquí podría agregar una verificación de estilo de código, por ejemplo con `eslint`:
  ```bash
  #! /bin/bash
  eslint .
  ```
- **Pre-push hook**: Antes de hacer push, correría las pruebas automáticas:
  ```bash
  #! /bin/bash
  npm test
  ```
- Esto evitaría que los desarrolladores suban código que no pasa las pruebas o no sigue las reglas de estilo, mejorando la calidad del código en la CI/CD.

---

## Ejercicio 4: Estrategias de branching en metodologías ágiles

**Pregunta**: ¿Cómo adaptarías la estrategia de branching para optimizar el flujo de trabajo?

**Respuesta**:
- Adoptaría una estrategia más simple como **GitHub Flow**, en lugar de **Git Flow**. Esto implica:
  - Trabajar en ramas feature cortas y fusionarlas a `main` lo antes posible.
  - Usar pull requests para garantizar revisiones de código antes de fusionar.
  
Con esto, se reducen las complicaciones al manejar muchas ramas y se evita el riesgo de conflictos grandes al final de un sprint.

---

## Ejercicio 5: Automatización de reversiones en CI/CD

**Pregunta**: ¿Cómo diseñarías un proceso automatizado para revertir cambios en una pipeline de CI/CD?

**Respuesta**:
- Si un bug crítico aparece, crearía un paso en la pipeline para ejecutar automáticamente un `git revert` y restaurar el sistema a un estado estable. Los pasos serían:
  1. Detectar el bug en la pipeline.
  2. Ejecutar `git revert <commit_hash>` en la rama principal.
  3. Correr las pruebas para verificar que todo funcione correctamente antes de continuar con otros desarrollos.
