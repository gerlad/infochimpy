##infochimpy

Infochimpy is a Python client library for the Infochimps API based on [tweepy](http://github.com/joshthecoder/tweepy). You might also want to look at [python-infochimps](https://github.com/geometrid/python-infochimps).

#### Using the shell.
Infochimpy is intended to be used from within an application, an example is [django-infochimps](https://github.com/gerlad/django-infochimps).

It may also be used through an interactive shell:

`$ ./chimpshell.py`

Launching the shell creates an api instance that will allow you to execute requests against the Infochimps API.

First you'll need to provide an api_key. 

`>> INFOCHIMPS_API_KEY = 'api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469'`

`>> api.trstrank('infochimps', INFOCHIMPS_API_KEY)`

> {u'screen_name': u'infochimps',
>  u'tq': u'94',
>  u'trstrank': u'3.21',
>  u'user_id': u'15748351'}

`>> api.influence('infochimps', INFOCHIMPS_API_KEY)`

> [result]

`>> api.wordbag('infochimps', INFOCHIMPS_API_KEY)`

> [result]

#### Available API commands
* _trstrank_        gets the trstrank and trstquotient for a given Twitter user
* _stronglinks_     finds all of the Strong Links of a given Twitter user
* _influence_       finds the level of inﬂuence for a given Twitter use
* _wordbag_         finds the words most associated with a given Twitter use
* _word_stats_      gets basic statistics associated with a given word on Twitter
* _conversations_   create data frame of recent conversations between two Twitter user
* _demographics_    gather demographic data for a given IP address from the U.S. Census
* _ip_geo_          IP address geo-location
* _census_          gathers U.S. Census data for a given IP address
* _domain_          returns domain information for a given domain

For more information on the Infochimps API see http://api.infochimps.com/.

#### Installation

If you haven't already we suggest you make use of pip. Following is an example environment for infochimpy.

_Install pip:_

`$ sudo easy_install -U pip`

_Install virtualenv:_

`$ sudo pip install -U virtualenv`

_Create a virtualenv._

`$ mkdir -p ~/Envs`

`$ cd ~/Envs`

`$ virtualenv --no-site-packages infochimps`

`$ source ~/Envs/bin/activate`

`(infochimps) cd /path/to/infochimpy`

`(infochimps) python setup.py install`

`(infochimps) ./chimpshell.py`

