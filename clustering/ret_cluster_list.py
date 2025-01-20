import pickle
from flask import jsonify
def ret_cluster_list(name):
    with open("final_list.txt", "rb") as fp:
        list_final = pickle.load(fp)
    for i in list_final:
        if name in i:
            print(type(i))
            return i
print(ret_cluster_list('Goa'))          
li = jsonify(ret_cluster_list('Orissa'))
ret_cluster_list('Meghalaya')
