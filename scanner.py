import bs4 as bs 
import re
import urllib

url = urllib.urlopen ("https://people.canonical.com/~ubuntu-security/cve/main.html").read()
soup = bs.BeautifulSoup (url, "lxml")

cve_id = []
pkg_name = []
vuln_status = []

'''
def ubuntu_data():

	"""Scrapes vulnerability status"""
	for tag in soup.find_all('tr'):
		##FIX ME: Presently, Appends a list to a list
		vuln_status.append(tag.get('class'))
	"""Scrapes package name and CVE ID"""
	for tag in soup.find_all('a'):
		href = tag.get ('href', None)
		"""Fix ME: Extract from tag attributes, to accomodate for future website changes, regex for speed """
		if re.findall ('^CVE.+', href):
			cve_id.append (href)
		##FIX ME: Presently, Appends a list to another list
		if re.findall ('\pkg+.*', href):
			pkg = re.findall ('pkg/(.+)\.html', href)
			pkg_name.append(pkg)
'''

def debian_data():

