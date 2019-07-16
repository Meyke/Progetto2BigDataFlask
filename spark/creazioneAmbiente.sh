#!/bin/bash


# Prima di fare la build dell'immagine modificare il file upload.py modificando l'indirizzo ip del cluster di elasticsearch


# build dell'immagine. 

docker build -t spark_image .

# creazione ed esecuzione del contenitore

docker run -it --name=spark_cont spark_image /bin/bash






