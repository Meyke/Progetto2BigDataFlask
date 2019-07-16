from pyspark.sql import SQLContext
from pyspark import SparkContext
sc = SparkContext("local", "First App")
sqlContext = SQLContext(sc)

df = sqlContext.read.csv("data/articles_1.csv",header=True)
df.describe
df = df.select("title","publication","content")
df.write.format("org.elasticsearch.spark.sql").option("es.nodes", "172.20.0.2:9200").option("es.resource", "news_idx/news").save()
