#!/usr/bin/python

import json
import collections

# primeste cheia parinte si cheia copil
# returneaza cheia compusa
# ex1: daca suntem pe primul nivel, parintele va fi sirul vid
    # deci cheia compusa va fi chiar cheia copil
# ex2: daca suntem pe al doilea nivel, cheia va fi compusa:
    # cheie_parinte.cheie_copil
def create_key(parent, child):
    if parent == "":
        new_key = child
    else:
        new_key = parent + "." + child
    return new_key

# primeste dictionarul si cheia din care acesta provine
# pentru dictionarul principal, cheia este sirul vid("")
def flatten(dict, key):
    result = ""

    # pentru fiecare pereche <cheie, valoare> din dictionar
    for k, v in dict.items():
        # daca valoarea este un dictionar, creez noua cheie
        # apelez functia recursiv pentru acest dictionar intern
        if isinstance(v, collections.Mapping):
            new_key = create_key(key, k)
            result += flatten(v, new_key)
        # daca valoarea nu este un dictionar, inseamna ca am ajuns finalul recursivitatii
        # adaug la rezultat intreaga cheie compusa si valoarea campului
        else:
            new_key = create_key(key, k)
            result += "\"" + new_key + "\"" + " : " + "\"" + str(v) + "\"" + "\n"

    return result

def unflatten(dict):
    result = ""

    # pentru fiecare pereche <cheie, valoare> din dictionar
    for k, v in dict.items():
        # daca valoarea este un dictionar
        # apelez functia recursiv pentru acest dictionar intern
        if isinstance(v, collections.Mapping):
            result += k + ": {\n" + unflatten(v) + "}"
        # daca valoarea nu este un dictionar, inseamna ca am ajuns finalul recursivitatii
        # adaug la rezultat cheia si valoarea pe care ma aflu
        else:
            result += "\"" + k + "\"" + " : " + "\"" + str(v) + "\"" + "\n"

    return result


# deschide fisierul care contine json-ul
with open('data.json') as json_file:
    data = json.load(json_file)

    # converteste dictionarul intr-unul ordonat
    # pentru a avea garantia ca parcurgerea se va face mereu la fel 
    data = collections.OrderedDict(data)

    result = flatten(data, "")
    # sterge ultimul caracter din resultat(new line-ul)
    result = result[:-1]
    print(result)

    print("")

    result = unflatten(data)
    # sterge ultimul caracter din resultat(new line-ul)
    print(result)

