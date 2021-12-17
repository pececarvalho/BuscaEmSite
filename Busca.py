# Busca no site do mercado livre
import requests
from bs4 import BeautifulSoup

url='https://lista.mercadolivre.com.br/'

produto_informado = input('Informe o produto: ')

#print(url+produto_informado)
response = requests.get(url+produto_informado)
#print(response.text)

# Usando BeautifulSoup
site = BeautifulSoup(response.text, 'html.parser')


produtos = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
for produto in produtos:
    #produto = site.find('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
    #print(site.prettify())
    #print(produto.prettify())
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
    print('Título do produto: ', titulo.text)

    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})
    print('Link do produto: ', link['href'])

    preco = produto.find('span', attrs={'class':'price-tag-text-sr-only'})
    print('R$ ', preco.text)
    print('\n\n')

