import requests
from bs4 import BeautifulSoup

# URL da página inicial do G1
url = 'https://g1.globo.com/'

# Fazer uma requisição HTTP para o site
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos os elementos que contêm as notícias
    # No G1, as notícias principais estão dentro de divs com a classe 'feed-post-body'
    noticias = soup.find_all('div', class_='feed-post-body')
    
    # Extrair informações de cada notícia
    for noticia in noticias:
        # Extrair o título
        titulo_tag = noticia.find('a', class_='feed-post-link')
        titulo = titulo_tag.get_text() if titulo_tag else 'Sem título'
        
        # Extrair o resumo
        resumo_tag = noticia.find('div', class_='feed-post-body-resumo')
        resumo = resumo_tag.get_text() if resumo_tag else 'Sem resumo'
        
        # Extrair o link
        link = titulo_tag['href'] if titulo_tag else 'Sem link'
        
        # Extrair a data/hora de publicação
        # No G1, isso geralmente está em uma tag <span> com a classe 'feed-post-datetime'
        data_tag = noticia.find('span', class_='feed-post-datetime')
        data = data_tag.get_text() if data_tag else 'Sem data'
        
        # Imprimir as informações coletadas
        print(f"Título: {titulo}")
        print(f"Resumo: {resumo}")
        print(f"Link: {link}")
        print(f"Data: {data}")
        print("-" * 80)
else:
    print(f"Falha ao acessar a página: {response.status_code}")