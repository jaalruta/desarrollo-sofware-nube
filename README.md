# Instrucciones de instalación
  A continuacíon se explican los pasos y requisitos que se deben cumplir para la correcta instalación de la aplicación
## Requisitos de maquina virtual
  Para la instalación de la maquina virtual se debe contar con una maquina virtual con lo siguientes requisitos minimos 
  - OS : [Ubuntu server 22.10](https://ubuntu.com/download/server)
  - Procesadores : 1Vcpu
  - Ram : 1GiB ram
  - Almacenamiento : 10GiB 


# Paso a paso
  ## Descarga de virtual box
   Para la descarga de virutual box que es el software que nos servira como hypervisor.
   - [Instalación en windows](https://www.geeksforgeeks.org/how-to-install-virtualbox-on-windows/)
   - [Instalación en linux](https://linuxconfig.org/install-virtualbox-on-ubuntu-20-04-focal-fossa-linux)
   - [Instalación en macOS](https://medium.com/analytics-vidhya/step-by-step-guide-to-download-and-install-virtual-box-in-macos-7341b6f99827)

  ## Instalar la maquina virtual
  Una vez descargada la imagen de [Ubuntu server 22.10](https://ubuntu.com/download/server) e instalado virtual box  ,debemos seguir los siguientes pasos
    Abriremos Virtual Box y daremos click sobre la siguiente opción.
  ![Captura de Pantalla 2022-10-23 a la(s) 10 14 36 a m](https://user-images.githubusercontent.com/98671337/197400243-9516377f-1736-48ca-8fdb-fe6ddd49b4c8.png)

  En la siguiente ventana ingresaremos el nombre de nuestra maquina virtual  y el tipo del sistema operativo
  ![imagen](https://user-images.githubusercontent.com/98671337/197400437-737ef82a-022e-4e35-927b-319aa7a96eba.png)

  Luego daremos click en siguiente y seleccionaremos la cantidad de memoria RAM que tendra la maquina virtual , para este caso como minimo 1GiB
 ![imagen](https://user-images.githubusercontent.com/98671337/197400520-686816c6-417e-4687-9fda-4c7041617992.png)
  
  Luego daremos click en siguiente y seleccionaremos la opción de crear un disco duro virtual
  ![imagen](https://user-images.githubusercontent.com/98671337/197400633-de41a1b7-0e3f-46f7-9cf9-b897e9bcf42d.png)

  Luego click en siguiente y seleccionaremos vdi
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197400642-7daba217-af54-4409-8b52-739094a572d7.png)
  
  Luego click en siguiente y seleccionaremos reservado dinamicamente

  ![imagen](https://user-images.githubusercontent.com/98671337/197400710-581c0ff0-128a-497f-af3a-80703ce65d96.png)

  Luego click en siguiente y seleccionaremos la cantidad de espacio de almacenamiento de la maquina virtual
  ![imagen](https://user-images.githubusercontent.com/98671337/197400774-19d8dca5-2a47-446b-8805-72d2c9f71fda.png)
 
  y por último click en crear
  ![imagen](https://user-images.githubusercontent.com/98671337/197400873-1e44af78-590b-4a3e-aef1-0fb422b576e7.png)
  
  Con esto ya tenemos la configuración inicial de nuestra maquina virtual
  
  # Instalar sistema operativo en la maquina virtual
  Debemos iniciar nuesrtra maquina virtual con el botón
  ![imagen](https://user-images.githubusercontent.com/98671337/197400981-179a3baa-f406-44b1-829d-a77211d7e29f.png)
  
  Luego nos pedira seleccionar la imagen con el sistema operativo
  ![imagen](https://user-images.githubusercontent.com/98671337/197401033-5063eb8e-983f-4546-ad81-fe1dfda076fb.png)
  
  En este punto debemos seleccionar la imagen de Ubuntu previamente descargada
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197401112-c74f10b8-5b33-490d-99da-0ed590740d47.png)
  
  Luego iniciarla la instalación
  ![imagen](https://user-images.githubusercontent.com/98671337/197401179-b46dded3-3558-4890-aa2d-a6466db9bb4e.png)
  
  Se nos preguntara que idioma queremos para nuestro sistema operativo , por defecto seleccionaremos Español
  ![imagen](https://user-images.githubusercontent.com/98671337/197401264-326b1fa9-ec2a-4728-b876-821fe802a773.png)
  ![imagen](https://user-images.githubusercontent.com/98671337/197401282-51596a00-101f-4425-afdb-f78f1ba1ddc6.png)
  
  En la siguiente pantalla seleccionaremos la opcion por defecto de ubuntu server
  ![imagen](https://user-images.githubusercontent.com/98671337/197401348-a4c3025a-9d5b-44ed-be38-76d36843bfa0.png)
  
  En opciones de red seleccionaremos la opción por defecto
  ![imagen](https://user-images.githubusercontent.com/98671337/197401375-beb79046-4796-4ff2-ae55-862aa53ec281.png)
  
  En la opción de proxy no especificaremos alguno
  ![imagen](https://user-images.githubusercontent.com/98671337/197401407-25beb126-8b03-49db-a411-aad0022ff7f1.png)
  
  En la opción de mirror address  seleccionaremos la opción por defecto
  ![imagen](https://user-images.githubusercontent.com/98671337/197401457-9fa606da-0c65-4aab-99a6-ab7612e808a9.png)

  Seleccionaremos la opcion de usar todo el disco duro
  ![imagen](https://user-images.githubusercontent.com/98671337/197401512-43a2b545-2c84-49b3-bd9e-1cfcd782238c.png)
  
  El las opciones de storage configuration seleccionaremos las opciones por defecto
  ![imagen](https://user-images.githubusercontent.com/98671337/197401576-e9fd0933-5484-423a-a36a-f893b9e2b48d.png)
  
  Luego ingresaremos la configuración del perfil
  ![imagen](https://user-images.githubusercontent.com/98671337/197401624-0f9c76e5-28c7-416a-a39e-3aa4944cd0ae.png)

  Nos preguntaran si queremos instalar algun snap , en esta seccion no seleccionaremos ninguno
  ![imagen](https://user-images.githubusercontent.com/98671337/197401749-6dcc71b6-525e-495b-83c1-fcc564806749.png)
  
  Iniciara la instalación del sistema operativo con la configuracíon previa
  ![imagen](https://user-images.githubusercontent.com/98671337/197401812-75be29c8-9b30-4c05-9c41-088d2b5ae09a.png)
  
  Una vez finalizada la instalaccion seleccionaremos la opción de reiniciar ahora
  ![imagen](https://user-images.githubusercontent.com/98671337/197401869-cfc8b25d-966b-4f9b-b540-1f54cd4471db.png)

  Cuando reinicie nos pedira nuestro usuario y contraseña y con eso se da como finalizada la instalacion del sistema operativo
  ![imagen](https://user-images.githubusercontent.com/98671337/197402191-d709460c-3b31-4db1-8825-cc6d5df21957.png)

## Requisitos de software de la aplicación
  Para la aplicación debemos contar con el siguiente software instalado en la maquina virtual (en cada uno de los enlaces esta la instrucción de instalación)
  ###Instalar redis
  para instalar redis debemos ejecitar el siguiente comando 
  ```
  sudo apt install redis-server
  ```
  
  para verificar que se instalo correctamente debemos ejecutar el siguiente comando
  ```
  redis-cli --version
  ```
  nos debera responder de una manera similar a esta
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197421841-c4300aa3-a9d2-4efa-bf80-63c4c7d70801.png)
  
  ###Instalar Postgresql
  
  Para instalar postgresql debemos ejecutar el siguiente comando
 
  ```
  sudo apt install postgresql postgresql-contrib
  ```
  para validar que se instalo de manera correcta debemos ejecutar el siguiente comando
  
  ```
  psql --version
  ```
  nos debera responder de una manera similar a esta
  ![imagen](https://user-images.githubusercontent.com/98671337/197421938-1a8d7138-6d0d-4b80-a32d-aa871107162e.png)
  
  ###Instalar ffmpeg
  
  Para instalar la libreria que nos ayudara a convertir archivos de audio debemo ejecutar el siguiente comando
  ```
  sudo apt update
  sudo apt install ffmpeg
  ```
  
  para validar que se instalo de manera correcta debemos ejecutar el siguiente comando
  
  ```
  ffmpeg -version
  ```
  nos debera responder de una manera similar a esta
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197422070-58511331-ab5e-4405-9544-aa248dff1442.png)

  ###Instalar git
  
  Normalmente git se instala por defecto en la version de ubuntu recomendada , para verificar la instalación se debe ejecutar el siguiente comando
  
  ```
  git --version
  ```
  
  si nos responde de una manera similar a esta git estara instalado
  ![imagen](https://user-images.githubusercontent.com/98671337/197422113-531bac03-460c-485f-a85e-de54f974eb6a.png)

  De lo contrario se deberan seguir las siguientes instrucciones
  
  [instalar git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  
  ###Instalar pip
  
  Una vez instalado lo anterior debemos ejecutar el siguiente comando para instalar pip
  
  ```
  sudo apt install python3-pip
  ```
  
  ### configuración de la base de datos
  
  Se debe ejecutar el siguiente comando para acceder al cliente por consola de postgresql
  
  ```
  sudo -u postgres psql
  ```
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197405325-08fe8766-9fd6-4cb0-8eee-7b445449b7b3.png)
  
  Luego debemos crear la base de datos con el siguiente comando
  
  ```
  CREATE DATABASE conversor;
  ```
  y luego 
  
  ```
   ALTER USER postgres WITH PASSWORD 'admin';
  ```
  y luego
  
  ```
  \q
  ```
  ### libreria entorno virtual python
  
  Se debe ejecutar el siguiente comando
  ```
  sudo apt install python3-venv
  ```
  
  ### configuración libreria postgresql
  
  Se debe ejecutar el siguiente comando
  ```
  sudo apt-get install libpq-dev
  ```
  ### intalacion gunicorn
  ```
  sudo apt install gunicorn
  ```

## instalacion de la aplicación

  Descargaremos la aplicacion desde el repositorio de git al escritorio de la maquina virtual
  
  ```
  git clone https://github.com/jaalruta/desarrollo-sofware-nube.git
  ```
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197415327-3d8a8ea4-3c45-459e-a515-2596f5d5f178.png)
  
  entraremos al la carpeta y crearemos el ambiente virtual
  ```
  cd desarrollo-sofware-nube
  python3 -m venv venv
  ```
  ![imagen](https://user-images.githubusercontent.com/98671337/197415497-a7103f57-8de0-469c-87e4-aa54f9614da7.png)
  
  activaremos el ambiente virtual
  ```
  . venv/bin/activate
  ```
  ![imagen](https://user-images.githubusercontent.com/98671337/197415544-1d55d410-64f8-4c21-8bf3-22267f6a99a5.png)

  
  Instalaremos las dependencias
  
  ```
  pip install -r requirements.txt
  ```
  
## ejecución de la aplicación
  
  ### Ejecutar la aplicación flask
  
  El siguiente comando nos permitira ejecutar la aplicación y verificar que no exista ningun problema
  ```
  flask run
  ```
  Debemos obtener un mensaje como el siguiente
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197420435-e2606d3a-46af-4345-bf9e-dc6c362e0536.png)

  luego de verificar que la aplicación se ejecuta correctamente deberemos detener su ejecución con
  ```
  CTRL + c
  ```
  
  ### Ejecutar Gunicorn
  
  Para ejecutar la aplicacion con gunicorn el cual nos permitira tener procesamiento en varios hilos, para esto usaremos el siguiente comando
  
  ```
  gunicorn -w 4 --bind 0.0.0.0:5000 wsgi:app --daemon
  ```
  
  con el siguiente comando podremos validar que se este ejecutando el proceso de gunicorn
  
  ```
  ps -aux | grep gunicorn
  ```
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197420647-e939e187-d436-4e02-a9c4-2be3280e988d.png)

  ### Ejecutar celery
  
  Para ejecutar celery usaremos el siguiente comando
  
  ```
  celery -A tareas.tareas worker -l INFO
  ```
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197420749-9e84dc81-5164-4f07-bf7e-b6eb5c49dbde.png)

  Con los pasos anteriores la aplicación estara lista para correr.
  
  ### Configuración adicional en virtual box si se quieren hacer peticiones con postman desdel el host
  
  Para poder conectar el host y la maquina virtual , se debe hacer lo siguiente
  
  Click en el boton configuracion
  ![imagen](https://user-images.githubusercontent.com/98671337/197420841-012c006b-043a-4f38-820e-567efe5215a1.png)


  Despues iremos a Red y desplegaremos las opciones avanzadas
  ![imagen](https://user-images.githubusercontent.com/98671337/197420874-af21492a-b0e5-4d20-9922-c8597f9db470.png)
  
  luego usaremos el boton reenvío de puertos
  
  En esta ventana debemos dar click en el boton
  ![imagen](https://user-images.githubusercontent.com/98671337/197420937-e179cea4-a5bb-4a9a-bc12-95b8505bf1c3.png)
  
  y luego procedemos a realizar el mapeo de la conexion con la maquina virtual
  ![imagen](https://user-images.githubusercontent.com/98671337/197420949-45a72bdb-2b25-42db-9f98-2039e8255d49.png)


  En la configuración de ejemplo cuando ingresen a la direccion 127.0.0.1 con puerto 6000 , el trafico sera redireccionado al puerto 5000 de la maquina virtual (notese que el apartado de ejemplo de la ejecución de gunicor se puso como puerto el 5000)

  con lo anterior podremos ejecutar desde postman en el host lss operaciones de la aplicacion que estan en la maquina virtual , en necesario apagar la maquina virtual y volver a ejecutarla para que tome la configuración
  
  
  ![imagen](https://user-images.githubusercontent.com/98671337/197421065-8fc82b57-3486-4e8c-be90-f86ce84ae1f9.png)


## Documentación de las operacion del servicio

La documentación puede ser consultada en el siguiente link








