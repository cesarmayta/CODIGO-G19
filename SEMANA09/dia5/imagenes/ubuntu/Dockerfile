#imagen base
FROM ubuntu

#comandos que ejecutare al crea la imagen
RUN apt-get update
RUN apt-get install python3 python3-dev -y

#definir un directorio de trabajo
WORKDIR /app

#copiar archivos al contenedor
COPY index.html .

#ejecutar un comando al iniciar el contenedor de la imagen
CMD python3 -m http.server 4000

#exponer puerto
EXPOSE 4000