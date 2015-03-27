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
        '//default:LineStatus[@ID="8"]/default:Line/@Name',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    espnine = root.xpath(
        '//default:LineStatus[@ID="8"]/default:Status/@Description',
        namespaces={'default': 'http://webservices.lul.co.uk/'}
    )
    statusnine = root.xpath(
        '//default:LineStatus[@ID="8"]/@StatusDetails',
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
    print(*statuseleven)


def menu():
    print('-' * 60)
    print('Welcome to the Tubey.py.\nThis code is operating under the GNU GPL 3.0 licence.'
          '\nData feed provided by Transport for London.\n'
          'Full Sourcecode at http://github.com/olipicard/tubestatus.py'
    )
    print('For a full list of commands type \'help\'')
    print('-' * 60)
loop = True
while loop:
    menu()
    convert = input('')
    words = re.findall(r'[a-z]|[A-Z]', convert)
    if words == ['q', 'u', 'i', 't']:  # or ['Q', 'U', 'I', 'T'] or ['Q', 'u', 'i', 't']:
        loop = False
    if words == ['Q', 'U', 'I', 'T']:
        loop = False
    if words == ['e', 'x', 'i', 't']:
        loop = False
    if words == ['E', 'X', 'I', 'T']:
        loop = False
    if words == ['h', 'e', 'l', 'p']:
        print('The following commands can be used.')
        print('-'*60)
        print('all lines')
        print('circle')
        print('central')
        print('bakerloo')
        print('district')
        print('hammersmithandcity')
        print('jubilee')
        print('metropolitan')
        print('northan')
        print('piccadilly')
        print('waterlooandcity')
        print('overground')
        print('dlr')
        escape = input('press any key to return back to the main menu.')
    if words == ['c', 'i', 'r', 'c', 'l', 'e']:
        circle()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l']:
        central()
        escape = input('press any key to return back to the main menu.')
    if words == ['C', 'E', 'N', 'T', 'R', 'A', 'L']:
        central()
        escape = input('press any key to return back to the main menu.')
    if words == ['C', 'e', 'n', 't', 'r', 'a', 'l']:
        central()
        escape = input('press any key to return back to the main menu.')
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        bakerloo()
        escape = input('press any key to return back to the main menu.')
    if words == ['B', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        bakerloo()
        escape = input('press any key to return back to the main menu.')
    if words == ['B', 'A', 'B', 'E', 'R', 'L', 'O', 'O']:
        bakerloo()
        escape = input('press any key to return back to the main menu.')
    if words == ['D', 'I', 'S', 'T', 'R', 'I', 'C', 'T']:
        district()
        escape = input('press any key to return back to the main menu.')
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't']:
        district()
        escape = input('press any key to return back to the main menu.')
    if words == ['D', 'i', 's', 't', 'r', 'i', 'c', 't']:
        district()
        escape = input('press any key to return back to the main menu.')
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        hammersmithandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['H', 'A', 'M', 'M', 'E', 'R', 'S', 'M', 'I', 'T', 'H', 'A', 'N', 'D', 'C', 'I', 'T', 'Y']:
        hammersmithandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['H', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        hammersmithandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['H', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'C', 'i', 't', 'y']:
        hammersmithandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['j', 'u', 'b', 'i', 'l', 'i', 'e', 'e']:
        jubilee()
    if words == ['J', 'u', 'b', 'i', 'l', 'i', 'e', 'e']:
        jubilee()
        escape = input('press any key to return back to the main menu.')
    if words == ['J', 'U', 'I', 'L', 'I', 'E', 'E']:
        jubilee()
        escape = input('press any key to return back to the main menu.')
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        metropolitan()
        escape = input('press any key to return back to the main menu.')
    if words == ['M', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        metropolitan()
        escape = input('press any key to return back to the main menu.')
    if words == ['M', 'E', 'T', 'R', 'O', 'P', 'O', 'L', 'I', 'T', 'A', 'N']:
        metropolitan()
        escape = input('press any key to return back to the main menu.')
    if words == ['m', 'e', 't']:
        metropolitan()
        escape = input('press any key to return back to the main menu.')
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n']:
        northan()
        escape = input('press any key to return back to the main menu.')
    if words == ['N', 'o', 'r', 't', 'h', 'a', 'n']:
        northan()
        escape = input('press any key to return back to the main menu.')
    if words == ['N', 'O', 'R', 'T', 'H', 'A', 'N']:
        northan()
        escape = input('press any key to return back to the main menu.')
    if words == ['n', 'o', 'r', 't', 'h']:
        northan()
        escape = input('press any key to return back to the main menu.')
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        piccadilly()
        escape = input('press any key to return back to the main menu.')
    if words == ['P', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        piccadilly()
        escape = input('press any key to return back to the main menu.')
    if words == ['P', 'I', 'C', 'C', 'A', 'D', 'I', 'L', 'L', 'Y']:
        piccadilly()
        escape = input('press any key to return back to the main menu.')
    if words == ['p', 'i', 'c']:
        piccadilly()
        escape = input('press any key to return back to the main menu.')
    if words == ['w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i','t', 'y']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['W', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'C', 'i', 't', 'y']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['W', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['W', 'A', 'T', 'E', 'R', 'L', 'O', 'O', 'A', 'N', 'D', 'C', 'I', 'T', 'Y']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['c', 'i', 't', 'y']:
        waterlooandcity()
        escape = input('press any key to return back to the main menu.')
    if words == ['o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        overground()
        escape = input('press any key to return back to the main menu.')
    if words == ['O', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        overground()
        escape = input('press any key to return back to the main menu.')
    if words == ['O', 'V', 'E', 'R', 'G', 'R', 'O', 'U', 'N', 'D']:
        overground()
        escape = input('press any key to return back to the main menu.')
    if words == ['D', 'L', 'R']:
        dlr()
        escape = input('press any key to return back to the main menu.')
    if words == ['d', 'l', 'r']:
        dlr()
        escape = input('press any key to return back to the main menu.')
    if words == ['a', 'l', 'l']:
        circle()
        central()
        bakerloo()
        district()
        hammersmithandcity()
        metropolitan()
        northan()
        jubilee()
        dlr()
        overground()
        escape = input('press any key to return back to the main menu.')
    if words == ['c', 'l', 'a', 's', 's', 'i', 'c']:
        classic()
        escape = input('press any key to return back to the main menu.')














