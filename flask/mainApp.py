from flask import Flask, render_template, jsonify, request, url_for
from elasticsearch import Elasticsearch
from fairnessModule import fairnessMethod
import logging
import numpy as np


app = Flask(__name__)

es = Elasticsearch()


@app.route("/")
@app.route("/risultati")
def homepage():
    return render_template("risultati.html")


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['ricerca']  # ho una form così chiamata in risultati.html

    body = {
        "from":0,"size":6,
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["content", "title"]
            }
        }
    }

    res = es.search(index="news_idx", body=body)
    hits = res['hits']['hits']
    # return jsonify(res['hits']['hits'])
    # nel caso volessi i risultati fair
    if request.form.get('Demographic Parity'):
        hits = fairnessMethod(hits,1)
    if request.form.get('Disparate Treatment'):
        hits = fairnessMethod(hits,2)
    if request.form.get('Disparate Impact'):
        hits = fairnessMethod(hits,3)

    dcg = round(calc_dcg(hits),2)


    return render_template("risultati.html", hits=hits, dcg=dcg)


def calc_dcg(hits, k=6):
  item_relevances = []
  for hit in hits:
      score = hit['_score']
      item_relevances.append(score)
  item_relevances = np.array(item_relevances)
  dropoff = np.log2(np.arange(len(item_relevances)) + 2.0)
  rel = 2 ** item_relevances - 1
  return np.sum(rel[:k] * 1.0 / dropoff[:k]).item()


if __name__ == "__main__":
    app.run(debug=True)
