__author__ = 'OliPicard'
from urllib.request import urlopen
from xml.dom import minidom
# Developed by OliPicard
# tubey.py is a simple line status console tool that provides live line status information via the TFL Cloud.
# this script is licenced under the GNU GPL 3.0 Licence (contained inside the git report at github.com/olipicard/tubey.py)
# tubey.py is provided free of charge and is 100% open sourced.

def resp():
    try:
        return minidom.parse(urlopen('http://cloud.tfl.gov.uk/TrackerNet/LineStatus'))
    except:
        print('Oh dear its seems the api has borked. Have you looked at the Azure status page?')
        return -1




def bakerloo(xmldoc):
    linestatus = xmldoc.getElementsByTagName('LineStatus')[0]
    status = linestatus.getElementsByTagName('Status')[0]
    linename = linestatus.getElementsByTagName('Line')[0]
    linestatusOne = linestatus.getAttribute('StatusDetails')
    statusOne = status.getAttribute('Description')
    linenameOne = linename.getAttribute('Name')
    print(' ')
    print(linenameOne + ' line')
    print(statusOne)
    print(linestatusOne)
    print(' ')

def central(xmldoc):
    linestatusb = xmldoc.getElementsByTagName('LineStatus')[1]
    statusi = linestatusb.getElementsByTagName('Status')[0]
    linenamei = linestatusb.getElementsByTagName('Line')[0]
    linestatusTwo = statusi.getAttribute('StatusDetails')
    statusTwo = statusi.getAttribute('Description')
    linenameTwo= linenamei.getAttribute('Name')
    print(' ')
    print(linenameTwo + ' Line')
    print(statusTwo)
    print(linestatusTwo)
    print(' ')

def circle(xmldoc):
    linestatusc = xmldoc.getElementsByTagName('LineStatus')[2]
    statusf = linestatusc.getElementsByTagName('Status')[0]
    linenameo = linestatusc.getElementsByTagName('Line')[0]
    linestatusThree = linestatusc.getAttribute('StatusDetails')
    statusThree = statusf.getAttribute('Description')
    linenameThree = linenameo.getAttribute('Name')
    print(' ')
    print(linenameThree + ' Line')
    print(statusThree)
    print(linestatusThree)
    print(' ')

def district(xmldoc):
    linestatusd = xmldoc.getElementsByTagName('LineStatus')[3]  # district line
    statusd = linestatusd.getElementsByTagName('Status')[0]  # status msg
    linenamep = linestatusd.getElementsByTagName('Line')[0]  # Line Name
    linestatusFour = linestatusd.getAttribute('StatusDetails')  # Detailed Msg about any problems
    statusFour = statusd.getAttribute('Description')  # description of the line status.
    linenameFour = linenamep.getAttribute('Name')  # line name
    print(' ')
    print(linenameFour + ' Line')
    print(statusFour)
    print(linestatusFour)
    print(' ')

def hammersmithandcity(xmldoc):
    linestatusp = xmldoc.getElementsByTagName('LineStatus')[4]
    statusp = linestatusp.getElementsByTagName('Status')[0]
    linenamef = linestatusp.getElementsByTagName('Line')[0]
    linestatusFive = linestatusp.getAttribute('StatusDetails')
    statusFive = statusp.getAttribute('Description')
    linenameFive = linenamef.getAttribute('Name')
    print(' ')
    print(linenameFive + " Line")
    print(statusFive)
    print(linestatusFive)
    print(' ')



def Jubilee(xmldoc):
    linestatusq = xmldoc.getElementsByTagName('LineStatus')[5]
    statusj = linestatusq.getElementsByTagName('Status')[0]
    linenamej = linestatusq.getElementsByTagName('Line')[0]
    linestatusSix = linestatusq.getAttribute('StatusDetails')
    statusSix = statusj.getAttribute('Description')
    linenameSix = linenamej.getAttribute('Name')
    print(' ')
    print(linenameSix + " Line")
    print(statusSix)
    print(linestatusSix)
    print(' ')

def Metropolitan(xmldoc):
    linestatusw = xmldoc.getElementsByTagName('LineStatus')[6]
    statusw = linestatusw.getElementsByTagName('Status')[0]
    linenamew = linestatusw.getElementsByTagName('Line')[0]
    linestatusSeven = linestatusw.getAttribute('StatusDetails')
    statusSeven = statusw.getAttribute('Description')
    linenameSeven = linenamew.getAttribute('Name')
    print(' ')
    print(linenameSeven + ' Line')
    print(statusSeven)
    print(linestatusSeven)
    print(' ')

def Northern(xmldoc):
    linestatuse = xmldoc.getElementsByTagName('LineStatus')[7]
    statuse = linestatuse.getElementsByTagName('Status')[0]
    linenamee = linestatuse.getElementsByTagName('Line')[0]
    linestatusEight = linestatuse.getAttribute('StatusDetails')
    statusEight = statuse.getAttribute('Description')
    linenameEight = linenamee.getAttribute('Name')
    print(' ')
    print(linenameEight + ' Line')
    print(statusEight)
    print(linestatusEight)
    print(' ')

def piccadilly(xmldoc):
    linestatusr = xmldoc.getElementsByTagName('LineStatus')[8]
    statusr = linestatusr.getElementsByTagName('Status')[0]
    linenamer = linestatusr.getElementsByTagName('Line')[0]
    linestatusNine = linestatusr.getAttribute('StatusDetails')
    statusNine = statusr.getAttribute('Description')
    linenameNine = linenamer.getAttribute('Name')
    print(' ')
    print(linenameNine + ' Line')
    print(statusNine)
    print(linestatusNine)
    print(' ')

def victoria(xmldoc):
    linestatust = xmldoc.getElementsByTagName('LineStatus')[9]
    statust = linestatust.getElementsByTagName('Status')[0]
    linenamer = linestatust.getElementsByTagName('Line')[0]
    linestatusTen = linestatust.getAttribute('StatusDetails')
    statusTen = statust.getAttribute('Description')
    linenameTen = linenamer.getAttribute('Name')
    print(' ')
    print(linenameTen + ' Line')
    print(statusTen)
    print(linestatusTen)
    print(' ')

def waterlooandcity(xmldoc):
    linestatusy = xmldoc.getElementsByTagName('LineStatus')[10]
    statusy = linestatusy.getElementsByTagName('Status')[0]
    linenamey = linestatusy.getElementsByTagName('Line')[0]
    linestatusEleven = linestatusy.getAttribute('StatusDetails')
    statusEleven = statusy.getAttribute('Description')
    linenameEleven = linenamey.getAttribute('Name')
    print(' ')
    print(linenameEleven + ' Line')
    print(statusEleven)
    print(linestatusEleven)
    print(' ')

def overground(xmldoc):
    linestatusu = xmldoc.getElementsByTagName('LineStatus')[11]
    statusu = linestatusu.getElementsByTagName('Status')[0]
    linenameu = linestatusu.getElementsByTagName('Line')[0]
    linestatusTweleve = linestatusu.getAttribute('StatusDetails')
    statusTweleve = statusu.getAttribute('Description')
    linenameTweleve = linenameu.getAttribute('Name')
    print(' ')
    print(linenameTweleve + ' Line')
    print(statusTweleve)
    print(linestatusTweleve)
    print(' ')

def dlr(xmldoc):
    linestatusi = xmldoc.getElementsByTagName('LineStatus')[12]
    statusi = linestatusi.getElementsByTagName('Status')[0]
    linenamei = linestatusi.getElementsByTagName('Line')[0]
    linestatusThirteen = linestatusi.getAttribute('StatusDetails')
    statusThirteen = statusi.getAttribute('Description')
    linenameThirteen = linenamei.getAttribute('Name')
    print(' ')
    print(linenameThirteen + ' Line')
    print(statusThirteen)
    print(linestatusThirteen)
    print(' ')

# calling the requests inbound. uncomment to manually call.
# bakerloo(resp())
# central(resp())
# circle(resp())
# district(resp())
# hammersmithandcity(resp())
# Jubilee(resp())
# Metropolitan(resp())
# Northern(resp())
# piccadilly(resp())
# victoria(resp())
# waterlooandcity(resp())
# overground(resp())
# dlr(resp())


def menu():
    print('-' * 60)
    print('Welcome to the TubeLineStatus.py application.\nThis code is operating under the GNU 3.0 licence.\nData feed provided by Transport for London.\nFull Sourcecode at http://github.com/olipicard/tubestatus.py')
    print('-' * 60)
    print('1. All Lines (will be slower to request.)')
    print('2. Bakerloo line')
    print('3. Central line')
    print('4. Circle line')
    print('5. District line')
    print('6. Hammersmith and City line')
    print('7. Jubilee line')
    print('8. Metropolitan line')
    print('9. Northan line')
    print('10. Piccadilly line')
    print('11. Victoria line')
    print('12. Waterloo and City line ')
    print('13. Overground')
    print('14. DLR')
    print('15. Terminate this application.')

loop = True
while loop:
    menu()
    choice=int(input('please enter a number from the menu. '))
    if choice not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        print('sorry the number you have picked is invaild. please pick again from the menu. ')
        menu()
        choice=int(input('please enter a number from the menu. '))
    if choice == 1:
        bakerloo(resp())
        central(resp())
        circle(resp())
        district(resp())
        hammersmithandcity(resp())
        Jubilee(resp())
        Metropolitan(resp())
        Northern(resp())
        piccadilly(resp())
        victoria(resp())
        waterlooandcity(resp())
        overground(resp())
        dlr(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 2:
        bakerloo(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 3:
        central(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 4:
        circle(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 5:
        district(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 6:
        hammersmithandcity(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 7:
        Jubilee(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 8:
        Metropolitan(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 9:
        Northern(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 10:
        piccadilly(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 11:
        victoria(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 12:
        waterlooandcity(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 13:
        overground(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 14:
        dlr(resp())
        escape = input('press any key to return back to the main menu.')
    if choice == 15:
        loop = False