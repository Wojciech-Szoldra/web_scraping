from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.pracuj.pl/praca/specjalista-ds-bezpieczenstwa-it-poznan-dolna-wilda-126,oferta,1003538768?s=bd289b9c&searchId=MTcyNDk2MjUyODQ0My4xOTI5&ref=top_booster_1_1_1')
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())