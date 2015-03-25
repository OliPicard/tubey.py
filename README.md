<h1>tubey.Py</h1>
tubey.py provides the latest line status by pulling data directly from Transport For London's Cloud API. The module requires no 3rd party resources and is very portable.

tubey.Py was built as a project for understanding how to program applications with XML apis.

<h2> Installation </h2>
You will need...

* [Python 3](http://python.org) runtime
* [requests](http://docs.python-requests.org/en/latest/#) type pip install requests
* Wheel type pip install Wheel
* [lxml](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) lxml whl file (lxml‑3.4.2‑cp34‑none‑win32.whl), Unfortunately the latest .exe build of lxml is outdated so we will need to build lxml via wheel. alternatively you can download the source version of lxml over at [pypi](https://pypi.python.org/pypi/lxml/3.4.2)

Once you have the wheel file launch up your command prompt/terminal and type pip install lxml‑3.4.2‑cp34‑none‑win32.whl then your installation of lxml should build!

(That about it! for this build.)


<h2>FAQ</h2>
<b> Why is lxml not compiling? </b>

lxml is rather problematic to get up and running on Windows systems, Thankfully Christoph Gohlke is providing wheel files that can be easily compiled with the wheel module by running a single command. As versions change Christoph updates the site in question. We have also provided a link to the offical pypi repo.

<b> Help! I'm getting an XML error when I attempt to run the code. </b>

The TFL API relies heavily on the Microsoft Azure cloud, it may be that the API is down or Azure is having an outage.

<b> Why are there two different versions of tubey.py? </b>
Originally I had planned to write the tubey.py application using urllib and xml.dom. While the project worked OK I noticed many issues with bugs. I decided to rewrite the application with the help of some friends over at /r/learnpython. After rewriting the application I could see huge performance and speed gains by using 3rd party modules.

The old version of the python script is known as tubeylegacy.py

The rewritten version of the script is now known as tubey.py

<h3>licence</h3>

The tubey.Py script is provided under the GNU GPL 3.0 License (Provided inside the Git Repo)

![GNU GPL 3.0](http://www.gnu.org/graphics/gplv3-127x51.png)

<h2>credits</h2>
Many Thanks to the wonderful people over at /r/learnpython.
a massive Thanks to __love__ for providing me information on how to return variables, Without your help this project wouldn't have gotten off the ground.

a massive thank you to /u/michaelkepler for providing a basic syntax to use with etree and integrate the requests module for handling XML files.

a massive thank you to stranac whom helped me understand xpath's application in data structures using the etree module. Your help to me and others on #Python freenode is awesome. Thank you for dedicating your time to helping others.


Many Thanks to the following 3rd party modules.
[LXML](http://lxml.de/) for the etree module
[Requests](http://docs.python-requests.org/en/latest/) for the awesome replacement for urllib.

Many Thanks to Transport for London for providing an awesome cloud based [tube line status](http://www.tfl.gov.uk/info-for/open-data-users/our-feeds) api.

Crafted with love by [OliPicard](https://olipicard.com)

if you liked this project consider looking at my [smart currency converter](https://github.com/OliPicard/smartcurrencyconvert.py) project.
