# Start by loading the required modules:
#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

# RUN FIRST OWASP ZAP ON YOUR COMPUTER
# GO TO MENU>TOOLS>OPTIONS>API
# THERE YOU CAN FIND Api Key AND OWASP ZAP LOCAL ADDRESS

# The value of api must match api.key when running the daemon
apiKey = 'your_owasp_zap_key'

# Define the target to scan:
target = 'http://127.0.0.1:5000'

# we can instantiate the zap instance, as follows:
# The following line must be the ip of where ZAP is, so the default is localhost:8080
# Also if you are not running ZAP on port 8080 then you must include the line below
# with the correct port numbers.
# This will instantiate a new instance with the assumption zap listens
# in the default port 8080. If Zap listens a non-default port, then
# we have to pass the custom proxy settings as the parameters, as follows:
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})


# TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')
# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))