from pymongo import  MongoClient

cliente = MongoClient('mongodb://localhost:27017/')

db = cliente.dbmidias

conexao = db.posts

#print(conexao.find_one())
#print(conexao.find({"nome":"José"}))

for conexao in conexao.find():
    print(conexao)