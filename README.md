Proyecto de una calculadora para la clase devops 2026 -2

- Se agregó `calculadora.py`: script de terminal para operaciones básicas (suma, resta, multiplicación y división).

## Explicación de comandos utilizados

- **`git init`**: Inicializa un repositorio local de Git en la carpeta actual.
- **`git add`**: Añade los archivos modificados o nuevos al área de preparación para incluirlos en el próximo commit.
- **`git commit`**: Guarda los cambios preparados en el historial del repositorio local junto con un mensaje descriptivo.
- **`git push`**: Sube o "empuja" los commits locales a la rama del repositorio remoto en GitHub.
- **`git status`**: Muestra el estado actual del área de trabajo (archivos modificados, en staging o sin seguimiento).
- **`git diff`**: Muestra las diferencias exactas línea por línea entre los archivos modificados y el último commit guardado.
- **`git log` / `git log --oneline --graph --all`**: Permite visualizar el historial de commits realizados; con flags adicionales los muestra en una sola línea y en forma de grafo visual.
- **`git restore`**: Descarta los cambios locales no guardados en un archivo, regresándolo al estado del último commit.
- **`git restore --staged`**: Saca un archivo del área de preparación (staging) tras haber usado `git add`, conservando las modificaciones intactas en el entorno local.
- **`git reset --soft HEAD~1`**: Deshace el último commit manteniendo todos los cambios preparados en el área de staging para modificarlos o volver a commitear.
- **`git checkout <hash> -- <archivo>`**: Restaura un archivo específico al contenido exacto que tenía en un commit anterior determinado.
- **`git branch -M`**: Renombra la rama actual (generalmente para definir `main` como rama principal).
- **`git remote add` / `git remote -v`**: `remote add` vincula el repositorio local con el repositorio remoto de GitHub; `remote -v` lista las conexiones remotas configuradas.
