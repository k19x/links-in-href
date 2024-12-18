import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def fetch_site_content(site):
    """Faz a requisição ao site e retorna o conteúdo HTML."""
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return None


def extract_links(site, html_content):
    """Extrai e normaliza os links encontrados no HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        # Normaliza a URL
        full_url = urljoin(site, link['href'])
        # Ignora links que apontam para o próprio site
        if site not in full_url:
            links.append(full_url)
    return links


def save_links_to_file(file_name, links):
    """Salva os links extraídos em um arquivo de texto."""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Links salvos em: {file_name}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def main():
    # Recebe entradas do usuário
    project_name = input("Digite o nome do projeto (arquivo): ")
    site = input("Insira a URL do site: ")

    # Valida a URL fornecida
    if not urlparse(site).scheme:
        print("URL inválida. Certifique-se de incluir 'http://' ou 'https://'.")
        return

    # Obtém o conteúdo do site
    html_content = fetch_site_content(site)
    if not html_content:
        return

    # Extrai os links
    links = extract_links(site, html_content)

    # Cria o arquivo de saída no diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{project_name}.txt")
    save_links_to_file(file_path, links)


if __name__ == "__main__":
    main()
