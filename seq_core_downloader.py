#!/usr/bin/env python3
# vim: fileencoding=utf-8
import requests
import lxml.html

from helpers import auth

BASE_URL = 'https://dna.cchmc.org/www/'

def get_results_download_links():
    """
    Log in to the Sequencing Core web site and get a list of download links
    """
    
    with requests.Session() as s:
        r = s.get(BASE_URL + 'main.php')
        assert r.ok

        (u,p) = auth.prompt_auth()
        r = s.post(BASE_URL + 'logon2.php',
                   data={'username': u, 'password': p})
        assert r.ok

        r = s.get(BASE_URL + 'main.php')
        assert r.ok

        html = lxml.html.fromstring(r.text)

        # get all the anchor tags within <ol><li> tags
        a_elems = html.xpath('//ol/li/a')

        for results_a in a_elems:
            r = s.get(BASE_URL + results_a.attrib['href'])
            assert r.ok
            html = lxml.html.fromstring(r.text)
            download_a = html.xpath('//a[b[contains(., "FULL DOWNLOAD")]]')[0]
            print(BASE_URL + download_a.attrib['href'])


if __name__ == '__main__':
    get_results_download_links()

