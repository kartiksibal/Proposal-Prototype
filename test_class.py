from mock import Mock
import pytest
import scanner as sc
from urllib import urlopen

"""Ubuntu data"""
ubuntu_fake_data = """
<tr class="High"> 
<td class="cve"><a href="CVE-2002-2439">CVE-2002-2439</a></td> 
<td class="pkg"><a href="pkg/gcc-4.4.html">gcc-4.4</a></td> 
<td class="needs-triage">needs-triage*</td> 
<td class="needs-triage">needs-triage</td> 
<td class="DNE">DNE</td> 
<td class="DNE">DNE</td> 
<td class="DNE">DNE</td> 
<td class="DNE">DNE</td> 
<td class="DNE">DNE</td> 
<td style="font-size: small;"><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-2439">Mitre</a> 
<a href="https://launchpad.net/bugs/cve/CVE-2002-2439">LP</a>
<a href="http://security-tracker.debian.org/tracker/CVE-2002-2439">Debian</a></td></tr>	
"""

"""Debian data"""
debian_fake_data = """
	<tr><td><a href="/tracker/source-package/389-ds-base">389-ds-base</a>
	</td><td><a href="/tracker/CVE-2016-5416">CVE-2016-5416</a>
	</td><td>not yet assigned</td><td>?</td></tr>
""" 

@pytest.mark.slow
def test_length():
	"""
	Checks for data consistency across
	both the datasets
	"""
	sc.ubuntu_data()
	sc.debian_data()
	assert len(sc.vuln_status) == len(sc.cve_id) == len (sc.pkg_name)

@pytest.mark.fast
def test_ubuntu_data():
	"""
	Checks for Ubuntu's data output
	"""	
	sc.urlopen = Mock()
	sc.urlopen.return_value = ubuntu_fake_data

	sc.ubuntu_data()
	
	assert sc.vuln_status[0] == "High" and sc.cve_id[0] == "CVE-2002-2439" and sc.pkg_name[0] == "gcc-4.4"

'''
##BUG##
@pytest.mark.fast
def test_debian_data():
	"""
	Checks for Debian's data output
	"""	
	sc.urlopen = Mock()
	sc.urlopen.return_value = debian_fake_data

	sc.debian_data()
	
	assert sc.vuln_status [1] == "not yet assigned" and sc.cve_id[1] == "CVE-2016-5416" and sc.pkg_name[1] == "389-ds-base"
'''


	
