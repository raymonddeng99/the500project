from os import listdir
from os.path import isfile, join
import fileinput
from bs4 import BeautifulSoup

def path_replace(src_dir):
	files = [f for f in listdir(src_dir) if isfile(join(src_dir, f)) and f.endswith('.html')]

	for single_file in files:
		soup = BeautifulSoup(open(src_dir + single_file), 'html.parser')

		links = soup.find_all(href=True)
		links = list(filter(lambda x: x['href'].endswith(('.css', '.ico', '.html', '.js')), links))

		for link in links:
			link['href'] = '../' + link['href']

		src_links = soup.find_all(src=True)
		src_links = list(filter(lambda x: x['src'].endswith(('.css', '.ico', '.html', '.js')), src_links))

		for link in src_links:
			link['src'] = '../' + link['src']


		with open(src_dir + single_file, 'w') as fp:
			fp.write(soup.prettify())


dirs = ['dist/article/', 'dist/work/']
for folder in dirs:
	path_replace(folder)