<h1>tubey.Py</h1>
tubey.py provides the latest line status by pulling data directly from Transport For London's Cloud API. The module requires no 3rd party resources and is very portable.

tubey.Py was built as a project for understanding how to program applications with XML apis.

<h2> Installation </h2>
You will need...

* [Python 3](http://python.org) runtime

(That about it! for this build. No 3rd party modules required.)


<h2>FAQ</h2>
<b> Why did you not use <insert 3rd party module here/> </b>

I decided to use xml.dom as the main scrapper method. It seemed very straight forward at the time. I had considered using lxml (a 3rd party module) however the module required additional dependencies. The wonderful people over at freenode's learn python did recommend suggest using etree method, This is something i'm looking at doing in the future as a faster rewrite. xml.dom works fine out of the box but is slower in comparison to some of the other methods mentioned.
<b> Help! I'm getting an XML error when I attempt to run the code. </b>

The TFL API relies heavily on the Microsoft Azure cloud, it may be that the API is down or Azure is having an outage.

<h3>licence</h3>

The tubey.Py script is provided under the GNU GPL 3.0 License (Provided inside the Git Repo)

![GNU GPL 3.0](http://www.gnu.org/graphics/gplv3-127x51.png)

<h2>credits</h2>
Many Thanks to the wonderful people over at /r/learnpython.
a massive Thanks to __love__ for providing me information on how to return variables, Without your help this project wouldn't have gotten off the ground.

Many Thanks to Transport for London for providing an awesome cloud based [tube line status](http://www.tfl.gov.uk/info-for/open-data-users/our-feeds) api.

Crafted with love by [OliPicard](https://olipicard.com)

if you liked this project consider looking at my [smart currency converter](https://github.com/OliPicard/smartcurrencyconvert.py) project.
