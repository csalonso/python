#imports
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from collections import Counter

try:
    #conectar a pagina
    html = urlopen('https://agilemanifesto.org/principles.html')
except HTTPError as e: #tratamento de HTTPError
    print(e)
except URLError as e: #tratamento de URLError
    print(e)
else:
    #ler html retornado pela pagina
    soup = BeautifulSoup(html.read(),'html.parser')

    #buscar tags na pagina
    tags = soup.findAll('p')

    texto = ''

    #recebe o texto de cada tag e guarda em uma unica variavel
    for tag in tags:
        texto = texto + (tag.getText())

    #exibe o texto completo
    print(texto)

    #conta quantas vezes uma palavra aparece no texto
    print('"agile" occurs ' + str(texto.lower().split().count('agile')) + ' times in the text')

    #verifica se uma palavra esta presente no texto
    if 'software' in texto:
        print('"software" occurs in the text')

    #exibe as 5 palavars que mais aparecem no texto
    c = Counter(texto.lower().split()).most_common(5)
    print(c)
