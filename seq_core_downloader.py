#!/usr/bin/env python3
# vim: fileencoding=utf-8
"""
Fetch download links from the CCHMC Sequencing Core web site
"""
import re
import argparse
import requests
import lxml.html

from helpers import auth  # for prompt_auth()

BASE_URL = 'https://dna.cchmc.org/www/'
CURL_CMD = 'curl -LOJ -C -'  # [silent: -s], follow redirects, use filename
                             # from header, and resume partial downloads

def get_results_download_links(with_curl=True):
    """
    Log in to the Sequencing Core web site and print list of download links

    If 'with_curl' is True, build curl command lines which include the
    authentication cookie (which you can pipe through 'bash' or 'parallel')
    """
    
    with requests.Session() as s:
        # one initial request to the "main" page is necessary to get a PHP
        # session ID
        r = s.get(BASE_URL + 'main.php')

        # assert that the response code is 2xx (200 series) = "no error"
        assert r.ok

        # auth.prompt_auth() returns a tuple of (username, password)
        (u,p) = auth.prompt_auth()
        r = s.post(BASE_URL + 'logon2.php',
                   data={'username': u, 'password': p})
        assert r.ok

        # make sure the response text has "LDAP login OK" in it; this
        # assertion will fail if you give invalid credentials because
        # re.search() will return None
        assert re.search('LDAP login OK', r.text)

        # this request will have the "authenticated" PHP session ID in it
        r = s.get(BASE_URL + 'main.php')
        assert r.ok

        # fetch the response text as an ElementTree that lxml can manipulate
        html = lxml.html.fromstring(r.text)

        # get all the <a> (anchor) tags within <ol><li> tags
        results_anchors = html.xpath('//ol/li/a')

        for a in results_anchors:
            r = s.get(BASE_URL + a.attrib['href'])
            assert r.ok
            html = lxml.html.fromstring(r.text)

            # results download link extracted from the parent <a>'s href
            # attribute which contains <b>FULL DOWNLOAD</b>; XPath magic
            # (source: https://stackoverflow.com/a/14631741)
            result_a = html.xpath('//a[b[contains(., "FULL DOWNLOAD")]]')[0]

            if with_curl:
                # Python string formatting:
                # https://docs.python.org/3/library/stdtypes.html#str.format
                cmd = "{curl} -H 'Cookie: PHPSESSID={sid}' '{url}'".format(
                          curl=CURL_CMD,
                          sid=s.cookies['PHPSESSID'],
                          url=BASE_URL + 'results/' + result_a.attrib['href']
                      )
                print(cmd)
            else:
                print(BASE_URL + result_a.attrib['href'])


# this "main guard" allows you to import this script as a module (from another
# script or an interactive session), but if you execute the script directly
# (e.g., ./seq_core_downloader.py), it runs the 'get_results_download_links'
# function
if __name__ == '__main__':
    # the magic variable '__doc__' is the module docstring (at the top)
    parser = argparse.ArgumentParser(
        description=__doc__.strip(),
        epilog="A Weirauch Lab production --"
               " bug reports: https://tf.cchmc.org/s/q1d9g")

    parser.add_argument('-c', '--curl', '--use-curl', '--with-curl',
                        help="create 'curl' command lines with the "
                             "authentication cookie already included",
                        action='store_true', dest='with_curl')
    options = parser.parse_args()
    
    get_results_download_links(options.with_curl)

