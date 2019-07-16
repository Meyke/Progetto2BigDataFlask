from flask import Flask, render_template, jsonify, request, url_for
from elasticsearch import Elasticsearch
from fairnessModule import fairnessMethod
import logging

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
    if request.form.get('fairness1'):
        hits = fairnessMethod(hits,1)
    if request.form.get('fairness2'):
        hits = fairnessMethod(hits,2)

    return render_template("risultati.html", hits=hits)


if __name__ == "__main__":
    app.run(debug=True)
