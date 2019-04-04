# Contenidos

Los contenidos que debes estudiar en la *semana x* están en la carpeta *semana x*. Si tienes dudas sobre el contenido puedes abrir una issue [aquí](https://github.com/IIC2233/syllabus/issues).

## Preguntas frecuentes

1. Yo abro los _notebooks_, hago cambios para ver como funcionan, y a la semana siguiente al hacer `git pull` me sale un error que dice "Your local changes to the following files would be overwritten by merge" ¿Qué puedo hacer?
    1. Siempre puedes clonar el repositorio otra vez, pero no es la idea. Lo que debes hacer es guardar tus cambios en alguna parte, hacer `pull`, y luego volver a aplicar tus cambios. Para eso coloca los siguientes comandos:
    
      ```bash
      git stash     # Guarda los cambios hechos en otra parte. Desaparecen del working directory.
      git pull      # El pull que queríamos hacer en un principio.
      git stash pop # Regresa los cambios hechos por ti al working directory.
      ```
