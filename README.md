Guía paso a paso de GitHub

1.	Claramente tener instalado Git.
2.	Configurar la identidad en el Gitbash

git config --global user.name "Tu Nombre"
git config --global user.email “ tu-email@example.com”

3.	Clonar el repositorio al equipo, puede ser con: 
-	Usando SSH:
git@github.com:joseboteropoli/proyecto-poli.git
-	Usando HTTPS:
https://github.com/joseboteropoli/proyecto-poli.git

4.	Entrar a la carpeta 
cd proyecto-poli

	Cada que se haga un cambio 
1.	Ver qué cambió:
git status

2.	Actualizar el proyecto antes de empezar
git pull origin main

3.	Guardar tus cambios

git add .      guarda todos los cambios 
git add  nombre_del _archivo/
	ej: git add frontend/
git commit -m "Descripción de lo que hice"

4.	Subir al repositorio:
git push origin main

Resumen 
o	git pull origin main → traer lo último.
o	Editar y programar.
o	git add .
o	git commit -m "mensaje claro"
o	git push origin main
Resumen add solo un archivo 
o	Usar git add nombre-carpeta/, para añadir solo la carpeta modificada.
o	Usar git add ruta/archivo si quieres ser aún más específico.
o	Luego se hace el commit y push normalmente.
