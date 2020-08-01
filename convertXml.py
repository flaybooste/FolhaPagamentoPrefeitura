import xml.etree.ElementTree as ET

def dados():
	tree = ET.parse('FolhaPagamento.xml')
	root = tree.getroot()
	meu = []
	for x in root:
		meu.append({
		"Competencia":x[0].text,
		"Lotacao":x[1].text,
		"Cargo":x[2].text,
		"NomeServidor":x[3].text,
		"SalarioBase":x[4].text,
		"Proventos":x[5].text,
		"Vantagens":x[6].text,
		"VencimentosTotais":x[7].text,
		"Descontos":x[8].text,
		"Liquido":x[9].text
		})
	return meu
