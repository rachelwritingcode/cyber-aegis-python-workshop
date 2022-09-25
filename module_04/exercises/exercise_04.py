from bs4 import BeautifulSoup

html_file = "./warmup.html"

with open(html_file) as file:
    soup = BeautifulSoup(file, "html.parser")
    h2_tag = soup.find_all("h2")
    print(h2_tag)