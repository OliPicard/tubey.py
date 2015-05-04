__author__ = 'OliPicard'
import requests
import sys

'''
tubey2.py provides you the latest information on tube disruptions.
This program is licenced under the GNU GPL 3.0 Licence.
The licence should be cloned along with the repo.
tubey2.py was developed by OliPicard.
+ Many thanks to James Singleton for alerting me to the new tfl json api.

'''

def menu():
    print('-' * 60)
    print('Welcome to the Tubey.py.\n'
          'This code is operating under the GNU GPL 3.0 licence.\nData feed provid'
          'ed by Transport for London.\nFull Sourcecode at http://github.com/olipicard/tubestatus.py')
    print('-' * 60)
    print('1. All Lines (will be slower to request.)')
    print('2. single station')
    print('3. exit this application')


def main():
    loop = True
    while loop:
        menu()
        choice = int(input('please enter a number from the menu. '))
        if choice not in [1, 2, 3]:
            menu()
            choice = int(input('please enter a number from the menu. '))
        if choice == 1:
            multistation()
            input('press any key to return back to the main menu.')
        if choice == 2:
            station()
            input('press any key to return back to the main menu.')
        if choice == 3:
            sys.exit()


def multistation():
    url = ('https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tram,'
           'national-rail,cable-car,river-bus,river-tour/status')
    b = requests.get(url)
    dataq = b.json()
    for i in dataq:
        print("{}".format(i['name']))
        for status in i['lineStatuses']:
            print("   {}".format(status['statusSeverityDescription']))
            if status['statusSeverity'] != 10:
                print("        {}".format(status['reason']))
        print('\n')


def station():
    url = 'https://api.tfl.gov.uk/Line/{0}/Status?'.format(input(' enter line:  '))
    print(url)
    a = requests.get(url)
    dataq = a.json()
    for i in dataq:
        print(i['lineStatuses'][0]['statusSeverityDescription'])




if __name__ == '__main__':
    main()
