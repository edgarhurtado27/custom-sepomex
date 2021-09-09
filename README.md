# About The Project

### Custom SEPOMEX
**https://custom-sepomex.herokuapp.com/**

El proyecto surge ante la necesidad de tener un servicio REST que sea capaz de entregar la entidad federativa y colonia a partir del código postal.
Si bien [SEPOMEX](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/Descarga.aspx) tiene un servicio en linea para consultar esta información, éste no es posible integrarlo de una forma eficiente con una aplicación web o móvil.

Con base en lo anterior el proyecto tiene sólo un **inbound rest api** de tipo GET, lo puedes consultar mandando una petición a la siguiente ruta:

* https://custom-sepomex.herokuapp.com/cp/:codigoPostal

**Toda la información devuelta por el servicio fue tomada directamente de [SEPOMEX](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/Descarga.aspx)**

#### Example Usage
Request
```sh
curl https://custom-sepomex.herokuapp.com/cp/56550
```
Response 
```sh
{"codigoPostal":"56550","colonias":["Emiliano Zapata","Derramadero"],"estao":"México","municipio":"Ixtapaluca"}
```
#### Built With
* [Python v3.6.14](https://www.python.org/)
* [Flask v2.0.1](https://flask.palletsprojects.com/en/2.0.x/)
* [Mongodb v5.0](https://www.mongodb.com/)


# Setup with Docker Compose

Esta sección detalla los pasos que debes seguir para hacer el setup del proyecto en tu ambiente local usando [Docker Compose](https://docs.docker.com/compose/)
#### Prerequisites
* [Docker v20.10.5](https://docs.docker.com/get-docker/)

#### Deploy

1. Clona el repositorio
   ```sh
   git clone git@github.com:edgarhurtado27/custom-sepomex.git
   ```
2. Construye la imagen e instancia un contenedor Docker
   ```sh
   docker-compose up -d
   ```
3. Valida que los contenedores **web-sepomex** y **mongo-sepomex** se estan online
   ```JS
   docker ps
   ```
4. Ejecuta el seeder para poblar la base de datos
   ```JS
   docker exec -it web-sepomex sh
   ```
   ```JS
   python customsepomex/seeder/curlSepomex.py
   ```

##### Usage

Una vez que el seeder finalice de importar la información, puedes realizar consultas de forma local

Request
```sh
curl curl localhost:5000/cp/40506
```
Response 
```sh
{"codigoPostal": "40506", "colonias": ["La Sidra (Puente Arroyo Seco)", "El Veladero", "Ojo de Agua", "Palapa"], "estado": "Guerrero", "municipio": "Arcelia" }
```
## Disclaimer
Recomiendo encarecidamente **no usar la aplicación desplegada en Heroku** para tus aplicaciones en ambientes productivos, las instancias en las que está desplegada tanto el servicio REST como la base de datos son gratuitas por lo que su procesamiento es limitado. En su lugar es preferible descargar el proyecto y desplegarlo en tus propios servidores y instancias, donde sólo tú o tu compañía tengan acceso.  

## Contributing
Este es mi primer proyecto con Python por lo que seguramente no seguí las mejores prácticas del lenguaje, así que las contribuciones son bienvenidas.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
# About The Project

### Custom SEPOMEX
**https://custom-sepomex.herokuapp.com/**

El proyecto surge ante la necesidad de tener un servicio REST que sea capaz de entregar la entidad federativa y colonia a partir del código postal.
Si bien [SEPOMEX](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/Descarga.aspx) tiene un servicio en linea para consultar esta información, éste no es posible integrarlo de una forma eficiente con una aplicación web o móvil.

Con base en lo anterior el proyecto tiene sólo un **inbound rest api** de tipo GET, lo puedes consultar mandando una petición a la siguiente ruta:

* https://custom-sepomex.herokuapp.com/cp/:codigoPostal

**Toda la información devuelta por el servicio fue tomada directamente de [SEPOMEX](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/Descarga.aspx)**

#### Example Usage
Request
```sh
curl https://custom-sepomex.herokuapp.com/cp/56550
```
Response 
```sh
{"codigoPostal":"56550","colonias":["Emiliano Zapata","Derramadero"],"estado":"México","municipio":"Ixtapaluca"}
```
#### Built With
* [Python v3.6.14](https://www.python.org/)
* [Flask v2.0.1](https://flask.palletsprojects.com/en/2.0.x/)
* [Mongodb v5.0](https://www.mongodb.com/)


# Setup with Docker Compose

Esta sección detalla los pasos que debes seguir para hacer el setup del proyecto en tu ambiente local usando [Docker Compose](https://docs.docker.com/compose/)
#### Prerequisites
* [Docker v20.10.5](https://docs.docker.com/get-docker/)

#### Deploy

1. Clona el repositorio
   ```sh
   git clone git@github.com:edgarhurtado27/custom-sepomex.git
   ```
2. Construye la imagen e instancia un contenedor Docker
   ```sh
   docker-compose up -d
   ```
3. Valida que los contenedores **web-sepomex** y **mongo-sepomex** se estan online
   ```JS
   docker ps
   ```
4. Ejecuta el seeder para poblar la base de datos
   ```JS
   docker exec -it web-sepomex sh
   ```
   ```JS
   python customsepomex/seeder/curlSepomex.py
   ```

##### Usage

Una vez que el seeder finalice de importar la información, puedes realizar consultas de forma local

Request
```sh
curl curl localhost:5000/cp/40506
```
Response 
```sh
{"codigoPostal": "40506", "colonias": ["La Sidra (Puente Arroyo Seco)", "El Veladero", "Ojo de Agua", "Palapa"], "estado": "Guerrero", "municipio": "Arcelia" }
```
## Disclaimer
Recomiendo encarecidamente **no usar la aplicación desplegada en Heroku** para tus aplicaciones en ambientes productivos, las instancias en las que está desplegada tanto el servicio REST como la base de datos son gratuitas por lo que su procesamiento es limitado. En su lugar es preferible descargar el proyecto y desplegarlo en tus propios servidores y instancias, donde sólo tú o tu compañía tengan acceso.  

## Contributing
Este es mi primer proyecto con Python por lo que seguramente no seguí las mejores prácticas del lenguaje, así que las contribuciones son bienvenidas.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

