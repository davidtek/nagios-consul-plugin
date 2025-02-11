#!/usr/bin/python
"""Usage: 
    check_consul_service_health SERVICE
        [--addr=ADDR]
        [--verbose]

Arguments:
    SERVICE  the consul service

Options:
    -h --help                  show this
    -v --verbose               verbose output
    --addr=ADDR                consul address [default: http://localhost:8500]

"""

from docopt import docopt
import requests, json, traceback, exceptions

def dump(it):
    if arguments['--verbose']: print it

def buildNodeUrl():
    url = "%(--addr)s/v1/health/checks/%(SERVICE)s" % arguments
    dump("Url: " + url)
    return url

def getJsonFromUrl(url):
    r = requests.get(url)
    dump("Response: " + r.text)
    dump("Status code: " + str(r.status_code))
    r.raise_for_status()
    return r.json()

def printCheck(check):
    print "> %(Node)s:%(ServiceName)s:%(Name)s:%(CheckID)s:%(Status)s" % check

def processFailing(checks):
    passing  = filter(lambda x: x['Status'] == 'passing', checks )
    warning  = filter(lambda x: x['Status'] == 'warning', checks)
    critical = filter(lambda x: x['Status'] == 'critical', checks)

    if len(checks) == 0:
        msg = "The service %(SERVICE)s does not exist in consul. The service may be down or not registered."  % arguments
        print msg
        return 1

    checkOutput = lambda x: x["Name"] + ":" + x["Output"]

    if len(critical):
        print "|".join(map(checkOutput, critical))
        for check in critical:
            printCheck(check)
    if len(warning):
        print "|".join(map(checkOutput, warning))
        for check in warning:
            printCheck(check)
    if len(passing):
        print "Passing: %d" % (len(passing))
        for check in passing:
            printCheck(check)

    return 2 if len(critical) else 1 if len(warning) else 0

if __name__ == '__main__':
    try:
        arguments = docopt(__doc__)
        dump("Arguments: " + str(arguments))
        url = buildNodeUrl()
        json = getJsonFromUrl(url)
        exit(processFailing(json))
    except exceptions.SystemExit: raise
    except:
        traceback.print_exc()
        exit(3)
