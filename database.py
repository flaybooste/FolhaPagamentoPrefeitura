from pymongo import MongoClient

def start():
    client = MongoClient("localhost", 27017)
    return client.folhapagamento.FolhaPag

def inserir(dado):
	return start().insert_one(dado).inserted_id

def selecionar():
	meu = []
	for x in start().find({}, {"_id":0,"NomeServidor": 1, "Liquido":2, "Cargo":3, "Lotacao":4}):
		meu.append(x)
	return meu