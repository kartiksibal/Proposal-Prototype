#!/usr/bin/env python

"""
This script scrapes package vulnerability info. from 
different datasets. It scrapes, CVE ID, Vulnerabiltiy 
Status & package name from different datasets and creates 
three list 'cve_id', 'pkg_name' & 'vuln_status', with all 
the scraped information
"""
import bs4 as bs 
import re
import sys

"""Py version check"""
if sys.version_info[0] == 3:
    from urllib.request import urlopen as ur
else:
    from urllib import urlopen as ur

cve_id = []
pkg_name = []
vuln_status = []
links = []

def ubuntu_data():
	
	"""Scrapes data from Ubuntu's 'Main' dataset"""
	url = ur("https://people.canonical.com/~ubuntu-security/cve/main.html").read()
	soup = bs.BeautifulSoup (url, "lxml")

	"""
	Scrapes vulnerability status.
	Ubuntu provides a general vulnerability 
	status of a package across all it's releases. 
	"""

	for tag in soup.find_all('tr'):
		
		if re.match('<\w+\s\w+="(\w+)">', str(tag)):
			status = re.findall('<\w+\s\w+="(\w+)">', str(tag))
			vuln_status.append(status[0])

	"""Scrapes package name and CVE ID"""
	for tag in soup.find_all('a'):
		
		href = tag.get ('href', None)

		if re.findall ('^CVE.+', href): 
			cve_id.append(href)
		
		if re.match('\pkg+.*', href):
			pkg = re.findall ('pkg/(.+)\.html', href)
			pkg_name.append(pkg[0])
	'''
	""" Uncomment to print scraped data"""
	for id in range(len(cve_id)):
		print ("\nCVE ID:{}\
			   \nPackage Name:{}\
			   \nStatus:{}".format(cve_id[id], 
				   		 		  pkg_name[id],
				                  vuln_status[id]))
	'''

def debian_data():
	
	"""Scrapes vulnerability data from Debian's dataset"""
	parent_url = ur ("https://security-tracker.debian.org/tracker/").read()
	soup = bs.BeautifulSoup (parent_url, "lxml")

	"""Extracts links of child datasets"""
	for tag in soup.find_all ('a'):
		
		href = tag.get('href')

		if re.findall('^/track+.*', href):
			links.append (href)

	for child_links in range (6):
		
		"""Extracts package info from all the child datasets"""
		child_url = ur ("https://security-tracker.debian.org" + links [child_links + 2]).read()
		soup = bs.BeautifulSoup (child_url, "lxml")

		for tag in soup.find_all ('a'):
			
			href = tag.get('href')
			
			if re.search('/tracker/CVE-(.+)', href):
				id = re.findall ('(?<=/tracker/).*', href)
				cve_id.append(id[0])
			
			if re.search('^/tracker/TEMP-+.*', href):
				id = re.findall ('(?<=/tracker/).*', href)
				cve_id.append(id[0])
			
			if re.search('/tracker/source-package/(.+)', href):
				pkg = re.findall ('(?<=/tracker/source-package/).*', href)
				pkg_name.append(pkg[0])
			
			"""if package name is empty, use the previous package name"""
			if href == "/tracker/source-package/":
				pkg_name.append(pkg)
		
		for tag in soup.find_all('td'):
			
			if "medium**" in tag or "medium" in tag or "low" in tag or "low**" in tag or "not yet assigned" in tag:
				vuln_status.append (tag.text)

			elif tag.find_all("span", {"class":"red"}) and tag.text == "high**" or tag.text == "high":
				vuln_status.append (tag.text)
		'''
		"""Uncomment to view scraped data"""
		for id in range(len(cve_id)):
			print ("\nCVE ID:{}\
			       \nPackage Name:{}\
			       \nStatus:{}".format(cve_id[id], 
				   		 			pkg_name[id],
				                 	vuln_status[id]))
		'''

if __name__ == '__main__':

	ubuntu_data()
	debian_data()
