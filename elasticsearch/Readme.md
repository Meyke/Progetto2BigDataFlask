
## Per avviare elasticsearch tramite docker, digitare:

docker run --name myelastic -p 9200:9200 -p 9300:9300 -v $(pwd)/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml elasticsearch:6.8.0

## Per stoppare il contenitore:
docker stop myelastic

## Per eliminare il contenitore:
docker rm myelastic

## Nota (se si vuol eseguire da un IDE in locale ed elasticsearch in contenitore docker):
Settare in elasticsearch.yml i seguenti (ho un volume condiviso col file presente in questa cartella)
 
transport.host: 0.0.0.0
xpack.security.enabled: false

Inoltre, in config della classe Config.java:
.put("client.transport.sniff", false)

In produzione posso usare una network o docker-compose.

