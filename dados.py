import json
from convertXml import dados
from database import inserir

for x in dados():
	inserir(x)