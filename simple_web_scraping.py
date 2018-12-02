# imports
from bs4 import BeautifulSoup  # biblioteca de web scraping
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from collections import Counter  # contador de objetos de coleção

try:
    # conectar a pagina
    html = urlopen('https://agilemanifesto.org/principles.html')
except HTTPError as e:  # tratamento de HTTPError
    print(e)
except URLError as e:  # tratamento de URLError
    print(e)
else:
    # ler html retornado pela pagina
    soup = BeautifulSoup(html.read(), 'html.parser')

    # buscar tags na pagina
    tags = soup.findAll('p')

    text = ''

    # receber o texto de cada tag e guarda em uma unica variavel
    for tag in tags:
        text = text + (tag.getText())

    # exibir o texto completo
    print(text)

    # dividir o texto
    splitted_text = text.lower().split()


    # contar quantas vezes uma palavra aparece no texto
    def count_word_in_text(word, text):
        c = str(text.count(word))
        print(word + ' occurs ' + c + ' times in the text')

    count_word_in_text('agile', splitted_text)
    count_word_in_text('software', splitted_text)


    # verificar se uma palavra esta presente no texto
    def word_in_text(word, text):
        if word in text:
            print(word + ' occurs in the text')


    word_in_text('software', splitted_text)
    word_in_text('agile', splitted_text)
    word_in_text('manifest', splitted_text)


    # exibir as 5 palavars que mais aparecem no texto
    def commom_words(text):
        c = Counter(text).most_common(5)
        print(c)


    commom_words(splitted_text)
