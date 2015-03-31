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
    print(*statuseleven)


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
        print('all')
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
        print('quit')
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
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e']:
        jubilee()
    if words == ['J', 'u', 'b', 'i', 'l', 'i', 'e', 'e']:
        jubilee()
        escape = input('press any key to return back to the main menu.')
    if words == ['J', 'U', 'B', 'I', 'L', 'I', 'E', 'E']:
        jubilee()
        escape = input('press any key to return back to the main menu.')
    if words == ['v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        victoria()
    if words == ['V', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        victoria()
    if words == ['V', 'I', 'C', 'T', 'O', 'R', 'I', 'A']:
        victoria()
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
    if words == ['w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
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
        piccadilly()
        victoria()
        jubilee()
        dlr()
        overground()
        escape = input('press any key to return back to the main menu.')
    if words == ['c', 'l', 'a', 's', 's', 'i', 'c']:
        classic()
        escape = input('press any key to return back to the main menu.')
    # merging words, wish me luck!
    if words == ['d', 'l', 'r', 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        dlr()
        overground()
    if words == ['d', 'l', 'r', 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        dlr()
        victoria()
    if words == ['d', 'l', 'r', 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        dlr()
        waterlooandcity()
    if words == ['d', 'l', 'r', 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        dlr()
        piccadilly()
    if words == ['d', 'l', 'r', 'c', 'i', 'r', 'c', 'l', 'e']:
        dlr()
        circle()
    if words == ['d', 'l', 'r', 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        dlr()
        central()
    if words == ['d', 'l', 'r', 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        dlr()
        bakerloo()
    if words == ['d', 'l', 'r', 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        dlr()
        district()
    if words == ['d', 'l', 'r',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        dlr()
        hammersmithandcity()
    if words == ['d', 'l', 'r', 'j', 'u', 'b', 'i', 'l', 'e' 'e']:
        dlr()
        jubilee()
    if words == ['d', 'l', 'r', 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        dlr()
        metropolitan()
    if words == ['d', 'l', 'r', 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        dlr()
        northan()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        circle()
        central()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        circle()
        overground()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        circle()
        piccadilly()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        circle()
        bakerloo()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        circle()
        district()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        circle()
        hammersmithandcity()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        circle()
        waterlooandcity()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'j', 'u', 'b', 'i', 'l', 'e' 'e']:
        circle()
        jubilee()
    if words == ['c', 'i', 'r', 'c', 'l', 'e', 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        circle()
        northan()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'd', 'l', 'r']:
        circle()
        dlr()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        circle()
        victoria()
    if words == ['c', 'i', 'r', 'c', 'l', 'e',
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        circle()
        metropolitan()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        central()
        overground()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        central()
        circle()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        central()
        bakerloo()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        central()
        district()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        central()
        hammersmithandcity()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'j', 'u', 'b', 'i', 'l', 'e' 'e']:
        central()
        jubilee()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        central()
        northan()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l', 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        central()
        metropolitan()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        central()
        victoria()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        central()
        piccadilly()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'd', 'l', 'r']:
        central()
        dlr()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        central()
        waterlooandcity()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l', 'c', 'i', 't', 'y']:
        central()
        waterlooandcity()
    if words == ['c', 'e', 'n', 't', 'r', 'a', 'l', 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        central()
        waterlooandcity()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o', 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        bakerloo()
        central()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        bakerloo()
        circle()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        bakerloo()
        district()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        bakerloo()
        hammersmithandcity()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        bakerloo()
        jubilee()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        bakerloo()
        metropolitan()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        bakerloo()
        northan()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        bakerloo()
        piccadilly()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        bakerloo()
        victoria()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        bakerloo()
        waterlooandcity()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        bakerloo()
        waterlooandcity()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o', 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        bakerloo()
        overground()
    if words == ['b', 'a', 'k', 'e', 'r', 'l', 'o', 'o', 'd', 'l', 'r']:
        bakerloo()
        dlr()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        district()
        bakerloo()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        district()
        central()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'c', 'i', 'r', 'c', 'l', 'e']:
        district()
        circle()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        district()
        hammersmithandcity()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h']:
        district()
        hammersmithandcity()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        district()
        jubilee()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        district()
        metropolitan()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        district()
        northan()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        district()
        piccadilly()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        district()
        victoria()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        district()
        waterlooandcity()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        waterlooandcity()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        district()
        overground()
    if words == ['d', 'i', 's', 't', 'r', 'i', 'c', 't', 'd', 'l', 'r']:
        district()
        dlr()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y'
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        hammersmithandcity()
        bakerloo()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        hammersmithandcity()
        central()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        hammersmithandcity()
        jubilee()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y'
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        hammersmithandcity()
        metropolitan()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        hammersmithandcity()
        northan()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        hammersmithandcity()
        piccadilly()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        hammersmithandcity()
        victoria()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        hammersmithandcity()
        overground()
    if words == ['h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y',
                 'd', 'l', 'r']:
        hammersmithandcity()
        dlr()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        jubilee()
        bakerloo()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e', 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        jubilee()
        central()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        jubilee()
        circle()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        jubilee()
        metropolitan()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        jubilee()
        northan()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'm', 'e', 't', 'r', 'o', 'p', 'l', 'i', 't', 'a', 'n']:
        jubilee()
        metropolitan()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        jubilee()
        piccadilly()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        jubilee()
        victoria()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        jubilee()
        waterlooandcity()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        jubilee()
        overground()
    if words == ['j', 'u', 'b', 'i', 'l', 'e', 'e',
                 'd', 'l', 'r']:
        jubilee()
        dlr()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        metropolitan()
        bakerloo()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        metropolitan()
        central()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        metropolitan()
        circle()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        metropolitan()
        district()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        metropolitan()
        hammersmithandcity()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h']:
        metropolitan()
        hammersmithandcity()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        metropolitan()
        jubilee()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        metropolitan()
        northan()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        metropolitan()
        piccadilly()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        metropolitan()
        northan()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        metropolitan()
        victoria()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        metropolitan()
        waterlooandcity()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n'
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        metropolitan()
        waterlooandcity()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        metropolitan()
        overground()
    if words == ['m', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n'
                 'd', 'l', 'r']:
        metropolitan()
        dlr()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        northan()
        bakerloo()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        northan()
        central()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        northan()
        circle()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        northan()
        district()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        northan()
        hammersmithandcity()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h']:
        northan()
        hammersmithandcity()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        northan()
        jubilee()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        northan()
        metropolitan()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y']:
        northan()
        piccadilly()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        northan()
        victoria()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        northan()
        waterlooandcity()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        northan()
        waterlooandcity()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        northan()
        overground()
    if words == ['n', 'o', 'r', 't', 'h', 'a', 'n',
                 'd', 'l', 'r']:
        northan()
        dlr()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        piccadilly()
        bakerloo()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y'
                 'c', 'e', 'n', 't', 'r', 'a', 'l']:
        piccadilly()
        central()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'c', 'i', 'r', 'c', 'l', 'e']:
        piccadilly()
        circle()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'd', 'i', 's', 't', 'r', 'i', 'c', 't']:
        piccadilly()
        district()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        piccadilly()
        hammersmithandcity()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'h', 'a', 'm', 'm', 'e', 'r', 's', 'm', 'i', 't', 'h']:
        piccadilly()
        hammersmithandcity()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'j', 'u', 'b', 'i', 'l', 'e', 'e']:
        piccadilly()
        jubilee()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'm', 'e', 't', 'r', 'o', 'p', 'o', 'l', 'i', 't', 'a', 'n']:
        piccadilly()
        metropolitan()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'n', 'o', 'r', 't', 'h', 'a', 'n']:
        piccadilly()
        northan()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a']:
        piccadilly()
        victoria()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o', 'a', 'n', 'd', 'c', 'i', 't', 'y']:
        piccadilly()
        waterlooandcity()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'w', 'a', 't', 'e', 'r', 'l', 'o', 'o']:
        piccadilly()
        waterlooandcity()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'o', 'v', 'e', 'r', 'g', 'r', 'o', 'u', 'n', 'd']:
        piccadilly()
        overground()
    if words == ['p', 'i', 'c', 'c', 'a', 'd', 'i', 'l', 'l', 'y',
                 'd', 'l', 'r']:
        piccadilly()
        dlr()
    if words == ['v', 'i', 'c', 't', 'o', 'r', 'i', 'a'
                 'b', 'a', 'k', 'e', 'r', 'l', 'o', 'o']:
        victoria()
        bakerloo()