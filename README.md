# ProgettoBigData2
Progetto per il corso di BigData

Il pdf è il report del progetto


## Creazione della rete (solo dopo aver avviato il contenitore con elasticsearch...andare nelle directory di interesse per avviarlo)

Per analizzare quali reti ho, digitare

```
docker network ls
```

```
docker network create BIGDATA

docker network inspect BIGDATA

docker network connect BIGDATA myelastic

```
Una volta avviato e inserito in rete il contenitore di Elasticsearch creare e avviare il contenitore con Spark(andare nella directory di interesse)

Successivamente inserire in rete anche il contenitore con Spark

```
docker network connect BIGDATA spark_cont

```

Una volta fatto ciò caricare da bash il dataset in Elasticsearch secondo istruzioni


Se il contenitore è avviato, per ottenere il suo ip:

```
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <name or id container>

```


# Per avviare l'applicazione con Flask andare nell'apposita cartella e seguire le indicazione nel Readme




