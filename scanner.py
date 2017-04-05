import bs4 as bs 
import re
import urllib

cve_id = []
pkg_name = []
vuln_status = []
links = []

def ubuntu_data():
	"""Scrapes data from Ubuntu's 'Main' dataset"""

	url = urllib.urlopen ("https://people.canonical.com/~ubuntu-security/cve/main.html").read()
	soup = bs.BeautifulSoup (url, "lxml")

	"""
	Scrapes vulnerability status.
	Ubuntu provides a general vulnerability 
	status of a package across all it's releases. 
	"""
	for tag in soup.find_all('tr'):
		vuln_status.append (tag.get ('class'))

	"""Scrapes package name and CVE ID"""
	for tag in soup.find_all('a'):
		
		href = tag.get ('href', None)

		if re.findall ('^CVE.+', href): 
			cve_id.append(href)
		
		if re.findall ('\pkg+.*', href):
			pkg = re.findall ('pkg/(.+)\.html', href)
			pkg_name.append(pkg)

def debian_data():
	"""Scrapes vulnerability data from Debian's dataset"""
	link = 2 
	parent_url = urllib.urlopen("https://security-tracker.debian.org/tracker/").read()
	soup = bs.BeautifulSoup (parent_url, "lxml")

	"""Extracts links of child datasets"""
	for tag in soup.find_all ('a'):
		
		href = tag.get('href')

		if re.findall('^/track+.*', href):
			links.append (href)

	for child_links in range (6):
		"""Extracts package info from all the child datasets"""
		child_url = urllib.urlopen("https://security-tracker.debian.org" + links [link]).read()
		link += 1		
		soup = bs.BeautifulSoup (child_url, "lxml")

		for tag in soup.find_all ('a'):
			
			href = tag.get ('href')
			
			if re.findall('/tracker/CVE-(.+)', href):
				id = re.findall ('(?<=/tracker/).*', href)
				cve_id.append (id)
			
			if re.findall ('^/tracker/TEMP-+.*', href):
				id = re.findall ('(?<=/tracker/).*', href)
				cve_id.append(id)
			
			if re.findall ('/tracker/source-package/(.+)', href):
				pkg = re.findall ('(?<=/tracker/source-package/).*', href)
				pkg_name.append (pkg)
			
			if href == "/tracker/source-package/":
				pkg_name.append (pkg)
		
		for tag in soup.find_all('td'):
			
			if "medium**" in tag or "medium" in tag or "low" in tag or "low**" in tag or "not yet assigned" in tag:
				vuln_status.append (tag.text)
			#BUG: Scrapes invalid data on 'testing' data
			elif soup.find_all("span", {"class":"red"}):
				vuln_status.append (tag.text)	

	# print len(cve_id), len (pkg_name), len (vuln_status)
	
	'''	
		"""Un-comment to view scraped data"""

		count = 0
		for i in cve_id:
			print "\nCVE ID:{}\
				   \nPackage Name:{}\
				   \nStatus:{}".format(cve_id[count][0], 
				   					 pkg_name[count][0],
				   					 vuln_status[count])
			count += 1
	'''
debian_data()
