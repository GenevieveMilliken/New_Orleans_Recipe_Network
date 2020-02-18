#scrapes classic New Orleans recipes from Saveur Magazine

from bs4 import BeautifulSoup
import requests
import re
import json
import time


all_my_recipes = []

url = "https://www.saveur.com/gallery/Classic-New-Orleans-Recipes/"

results_page = requests.get(url)
results_page_html = results_page.text
soup = BeautifulSoup(results_page_html, "html.parser")

recipes = soup.find_all('h3')

my_recipe_data = {
	"title" : None, 
	# "url" : None,
	# "text": None,
	"ingredients" : None,
	# "instructions" : None,
}

for recipe in recipes:

	print("----------------")

	title = recipe.find('a')
	title_text = title.text
	# my_recipe_data['title'] = title_text
	# print(title_text)

	url = title['href']
	url = "https://www.saveur.com/" + url
	my_recipe_data['url'] = url
	

	recipe_request = requests.get(url)
	recipe_html = recipe_request.text
	recipe_soup = BeautifulSoup(recipe_html, "html.parser")
	
	ingredients = recipe_soup.find('ul', attrs={"class": "ingredients"})
	ingredients = ingredients.text
	ingredients = ingredients.replace('\n', ";")
	ingredients = ingredients.replace(";;;", "; ")
	ingredients = ingredients.replace(";; ", "")
	my_recipe_data['ingredients'] = ingredients

	all_my_recipes.append()

	time.sleep(5)


