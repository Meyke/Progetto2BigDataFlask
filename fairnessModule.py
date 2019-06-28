
## QUI ANDIAMO A DEFINIRE I METODI DI FAIRNESS
## guardare qui https://github.com/dmh43/fair-ranking
def fairnessMethod(hits):
    for hit in hits:
        hit['_source']['title'] = hit['_source']['title'] + " (fair ahahahaha)"
    return hits