import json, os
try:
    # For python3
    import urllib.error
    import urllib.parse
    import urllib.request
except:
    # For python2
    import imp
    import urllib2
    import urlparse
    urllib = imp.new_module('urllib')
    urllib.error = urllib2
    urllib.parse = urlparse
    urllib.request = urllib2
try:
    devices = []
    url = "https://raw.githubusercontent.com/PixelExperience/official_devices/master/devices.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for res in data:
        for version in res['supported_versions']:
            if not os.path.exists('_data/devices/' + res['codename'] + '.yml') and res['codename'] not in devices:
                devices.append(res['codename'])
                print (res['codename'] + ' not found')
except:
    print ("")