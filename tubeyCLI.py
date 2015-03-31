__author__ = 'OliPicard'
from lxml import etree
import requests
import re
'''
-----------------------------------------------------------------
tubey.py provides you the latest information on tube disruptions.

This program is licenced under the GNU GPL 3.0 Licence.
The licence should be cloned along with the repo.

tubey.py was developed by OliPicard.

+ fixed formatting (https://github.com/OliPicard/tubey.py/pull/1)
Thanks to Kenneth Love for the heads up and patch code.
+ removed regex in exchange for simplified
-----------------------------------------------------------------
'''

'''
----------------------
|HTTP (Do NOT change)|
----------------------
'''
url = 'http://cloud.tfl.gov.uk/TrackerNet/LineStatus'
resp = requests.get(url)  # grabbing url data via requests
resp.encoding = 'utf-8'
xmldoc = resp.text  # saving the response as text (requests cannot handle xml)

root = etree.fromstring(xmldoc)  # parsing xml from text






def classic():
    for tube_line in root:  # grabs all current data feeds. Thanks to reddit user /u/michaelkepler for providing this code.
        # line_id = tube_line[1].get('ID')
        line_name = tube_line[1].get('Name')
        line_status = tube_line[2].get('Description')
        status_details = tube_line.get('StatusDetails')
        print(line_name, line_status, status_details)


def bakerloo():  # thanks to stranac for explaining xpath to me
    namezero = root.xpath(  # Thanks to Kenneth Love (__love__) for formatting patch.
        '//default:LineStatus[@ID="0"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espzero = root.xpath(
        '//default:LineStatus[@ID="0"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statuszero = root.xpath(
        '//default:LineStatus[@ID="0"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namezero.append('Line')
    print(*namezero)
    print(*espzero, sep='\n')
    print(*statuszero)


def central():
    nameone = root.xpath(
        '//default:LineStatus[@ID="1"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espone = root.xpath(
        '//default:LineStatus[@ID="1"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusone = root.xpath(
        '//default:LineStatus[@ID="1"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    nameone.append('Line')
    print(*nameone)
    print(*espone, sep='\n')
    print(*statusone)


def circle():
    nameten = root.xpath(
        '//default:LineStatus[@ID="10"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    esp = root.xpath(
        '//default:LineStatus[@ID="10"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusten = root.xpath(
        '//default:LineStatus[@ID="10"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    nameten.append('Line')
    print(*nameten)
    print(*esp, sep='\n')
    print(*statusten, sep='\n')

def district():
    nametwo = root.xpath(
        '//default:LineStatus[@ID="2"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    esptwo = root.xpath(
        '//default:LineStatus[@ID="2"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statustwo = root.xpath(
        '//default:LineStatus[@ID="2"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    nametwo.append('Line')
    print(*nametwo)
    print(*esptwo, sep='\n')
    print(*statustwo)

def hammersmithandcity():
    namethree = root.xpath(
        '//default:LineStatus[@ID="8"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espthree = root.xpath(
        '//default:LineStatus[@ID="8"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusthree = root.xpath(
        '//default:LineStatus[@ID="8"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namethree.append('Line')
    print(*namethree)
    print(*espthree, sep='\n')
    print(*statusthree)

def jubilee():
    namefour = root.xpath(
        '//default:LineStatus[@ID="4"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espfour = root.xpath(
        '//default:LineStatus[@ID="4"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusfour = root.xpath(
        '//default:LineStatus[@ID="4"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namefour.append('Line')
    print(*namefour)
    print(*espfour, sep='\n')
    print(*statusfour)

def metropolitan():
    namefive = root.xpath(
        '//default:LineStatus[@ID="9"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espfive = root.xpath(
        '//default:LineStatus[@ID="9"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusfive = root.xpath(
        '//default:LineStatus[@ID="9"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namefive.append('Line')
    print(*namefive)
    print(*espfive, sep='\n')
    print(*statusfive)

def northan():
    namesix = root.xpath(
        '//default:LineStatus[@ID="5"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espsix = root.xpath(
        '//default:LineStatus[@ID="5"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statussix = root.xpath(
        '//default:LineStatus[@ID="5"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namesix.append('Line')
    print(*namesix)
    print(*espsix, sep='\n')
    print(*statussix)

def piccadilly():
    nameseven = root.xpath(
        '//default:LineStatus[@ID="6"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espseven = root.xpath(
        '//default:LineStatus[@ID="6"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusseven = root.xpath(
        '//default:LineStatus[@ID="6"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk'}
    )
    nameseven.append('Line')
    print(*nameseven)
    print(*espseven, sep='\n')
    print(*statusseven)

def victoria():
    nameeight = root.xpath(
        '//default:LineStatus[@ID="7"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espeight = root.xpath(
        '//default:LineStatus[@ID="7"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statuseight = root.xpath(
        '//default:LineStatus[@ID="7"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    nameeight.append('Line')
    print(*nameeight)
    print(*espeight, sep='\n')
    print(*statuseight)

def waterlooandcity():
    namenine = root.xpath(
        '//default:LineStatus[@ID="11"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espnine = root.xpath(
        '//default:LineStatus[@ID="11"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusnine = root.xpath(
        '//default:LineStatus[@ID="11"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    namenine.append('Line')
    print(*namenine)
    print(*espnine, sep='\n')
    print(*statusnine)

def overground():
    nameten = root.xpath(
        '//default:LineStatus[@ID="82"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espten = root.xpath(
        '//default:LineStatus[@ID="82"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusten = root.xpath(
        '//default:LineStatus[@ID="82"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    print(*nameten)
    print(*espten, sep='\n')
    print(*statusten)

def dlr():
    nameeleven = root.xpath(
        '//default:LineStatus[@ID="81"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espeleven = root.xpath(
        '//default:LineStatus[@ID="81"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statuseleven = root.xpath(
        '//default:LineStatus[@ID="81"]/@StatusDetails',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    print(*nameeleven)
    print(*espeleven, sep='\n')
    print(*statuseleven

def bakerloocentral():
    bakerloo()
    central()

def quit():
    menu.loop = False


def menu():
    print('-' * 60)
    print('Welcome to the Tubey.py.\nThis code is operating under the GNU GPL 3.0 licence.'
          '\nData feed provided by Transport for London.\n'
          'Full Sourcecode at http://github.com/olipicard/tubestatus.py')
    print('For a full list of commands type \'help\'')
    print('-' * 60)
loop = True
while loop:
    menu()
    words = input('').lower()  # Thanks to Wub Wub for helping me re-engineer this segment minus regex pattens.
    available_functions = {'bakerloo': bakerloo,
                           'central': central,
                           'central bakerloo': lambda: central() or bakerloo()}
    try:
        if words == "help":
            for key in available_functions.keys():
                print(key)
                continue
        if words == "quit":
            loop = False
        available_functions[words]()
    except KeyError:
        print('Whoops!')