# Instrucciones de instalacion
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
  - [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
  - [Postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)
  - [ffmpeg](https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-20-04/)
  - [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)









  






