from bs4 import BeautifulSoup

html_file = "./secret_website.html"

with open(html_file) as file:
    soup = BeautifulSoup(file, "html.parser")
    p_tags = soup.find_all("p")
    
    for p_tag in p_tags:
        print(p_tag)