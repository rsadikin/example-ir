import requests
from bs4 import BeautifulSoup

def GetVisibleText(url="https://www.lipi.go.id"):
	res = requests.get(url)
	html_page = res.content
	soup = BeautifulSoup(html_page, 'html.parser')
	text = soup.find_all(text=True)

	output = ''
	blacklist = [
		'[document]',
		'noscript',
		'header',
		'html',
		'meta',
		'head', 
		'input',
		'script',
		# there may be more elements you don't want, such as "style", etc.
	]

	for t in text:
		if t.parent.name not in blacklist:
			output += '{} '.format(t)
	return output.encode('ascii','ignore').decode('ascii')

