import wget

a = 2010
m = 1

for a in range(2010,2017):
    for m in range(1,13):
        wget.download('http://arquivos.portaldatransparencia.gov.br/downloads.asp?a={0}&m={1:02}&consulta=CPGF'.format(a, m))
