# Spark per caricare il dataset in Elasticsearch

### Installazione e avvio dell'ambiente

Il seguente script builda e avvia un contenitore in cui è possibile utilizzare Spark per caricare i dati in Elasticsearch. Per avviare il contenitore eseguire lo script:

```
chmod 777 creazioneAmbiente.sh 
./creazioneAmbiente.sh
```

Una volta inserito in rete il contenitore eseguire da bash i seguenti comandi

```
cd spark-2.4.3-bin-hadoop2.7 
./bin/spark-submit data/upload.py
```

### comandi utili 

Per stoppare (attenzione, non rimuovere) il contenitore con nome *face_rec_cont*:

```
docker stop face_rec_cont
```
Per avviare il contenitore in modo interattivo:

```
docker start -i face_rec_cont
```

**ATTENZIONE**: se eliminiamo un contenitore, viene eliminato anche il suo contenuto. Questo può essere evitato montando un VOLUME linkato con qualche cartella del proprio host. Si guardi la documentazione di docker.

### Altro

Il file articles_1.csv contiene solo un sottoinsieme dell'intero dataset...per utilizzare l'intero dataset scaricarlo da https://www.kaggle.com/snapcrack/all-the-news, unire i 3 csv in un file solo e sostituirlo al csv presente con lo stesso nome
