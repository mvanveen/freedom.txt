freedom.txt
===========

### Introduction

Publicly announce your support against internet censorship!  

Join the dozens who have already pledged their support.

### Links 

* [My freedom.txt](http://www.mvanveen.net/freedom.txt).
* [Project website](http://wastedcode.com/freedom/).
* [Inderpreet's  original blog post][isingh] for more information

### Generate Your Own

Running `freedom.py` from the command line will generate a fresh `freedom.txt` 
file after a little prompting.

Add your new link to locations.txt as a seperate line in order to have the script 
automattically add it.

The following will add a custom `freedom.txt` into the local directory:

    $ python freedom.py 
    What is your name? Michael Van Veen
    Hi, my name is Michael Van Veen and I own this website.
    
    I no longer wish to stay anonymous in the fight against Internet
    censorship and those who want to close down our Internet.
    
    An open Internet is more important than the interests of nation
    states.
    
    An open Internet is more important than corporations.
    
    An open Internet is more important than security, copyright
    infringement, terrorism or child pornography.
    
    Many governments have failed us because of ignorance and corruption;
    they must be fought. Many corporations have failed us because of
    their greed; they must be changed.
    
    The interests of a few are not more important than the freedoms of
    all, whether those interests are seeded in greed, control, religion,
    or the false promises of security.
    
    We will not be fooled by the strategies of fear employed by those
    who wish to censor us.
    
    A closed internet is a tool of oppression. An open internet is a
    weapon of mass creation. Pick your sides. Create your own freedom.txt
    on your websites. Use this freedom.txt as a template, if you'd like,
    or head to freedomtxt.org for more information.
    
    Thank you for reading.
    
    _____________________________________________________________________
    
    "I would rather be exposed to the inconveniences attending too much
    liberty than to those attending too small a degree of it."
    - Thomas Jefferson
    
    ---
    humans:
      http://dagrevis.lv/freedom.txt: 178.79.160.88
      http://danmcewan.com/freedom.txt: 173.230.131.140
      http://dudmail.com/freedom.txt: 74.50.61.206
      http://fr.anc.is/freedom.txt: 208.94.116.57
      http://hoop-la.ca/freedom.txt: 70.66.72.121
      http://jacobroufa.com/freedom.txt: 173.236.211.83
      http://kyleterry.com/freedom.txt: 173.255.214.107
      http://mvanveen.net/freedom.txt: 173.236.202.225
      http://nul.co.za/freedom.txt: 216.246.55.83
      http://ulrichard.ch/freedom.txt: 62.202.65.166
      http://www.fermasoft.com/freedom.txt: 62.149.140.13
      http://www.isingh.info/freedom.txt: 66.147.244.74
      http://www.nicollet.net/freedom.txt: 87.98.188.226
      http://www.roleplaygateway.com/freedom.txt: 173.203.107.43
      https://www.jacobsparts.com/freedom.txt: 64.255.252.123
    poi:
      http://news.ycombinator.com/: 174.132.225.106
      http://twitter.org/: 69.6.27.100
      http://www.eff.org/: 69.50.232.54
      http://www.github.com/: 207.97.227.243
      http://www.google.com/: 74.125.224.116
      http://www.wikipedia.org/: 208.80.152.201
    ---
    
### /etc/hosts Integration

**experimental**: *Now supports `/etc/hosts` integration!*

Running with the `--with-hosts` flag will add in your `/etc/hosts` file.

    hosts_file:
      broadcasthost:
        - 255.255.255.255
      localhost:
        - 127.0.0.1
        - ::1
        - fe80::1%lo0

The `--hosts-file` switchoff will let you specify a custom hosts location to read from.

Finally, `--write-hosts` will write a `HOSTS` file in your local directory.

    $python freedom.py --hosts-file=/etc/hosts --write-hosts

*default output ensues...*

    writing file [HOSTS]... OK

    $ freedom.txt git:(etc_hosts) ✗ cat HOSTS

    173.230.131.140         danmcewan.com
    173.236.211.83          jacobroufa.com
    178.79.160.88           dagrevis.lv
    208.80.152.201          www.wikipedia.org
    69.50.232.54            www.eff.org
    69.6.27.100             twitter.org
    74.125.224.112          www.google.com
    207.97.227.243          www.github.com
    74.50.61.206            dudmail.com
    70.66.72.121            hoop-la.ca
    66.147.244.74           www.isingh.info
    208.94.116.12           fr.anc.is
    64.255.252.123          www.jacobsparts.com
    173.236.202.225         mvanveen.net
    255.255.255.255         broadcasthost
    173.203.107.43          www.roleplaygateway.com
    174.132.225.106         news.ycombinator.com
    127.0.0.1               localhost
    ::1                     localhost
    fe80::1%lo0             localhost
    173.255.214.107         kyleterry.com
### Adding links

For now, send me a pull request with your link and I'll include it.

I plan to add a command line arg to add links automattically in the near future.

### Currently Displayed Locations

* [http://fr.anc.is/freedom.txt](http://fr.anc.is/freedom.txt)
* [http://www.roleplaygateway.com/freedom.txt](http://www.roleplaygateway.com/freedom.txt)
* [http://danmcewan.com/freedom.txt](http://danmcewan.com/freedom.txt)
* [http://dudmail.com/freedom.txt](http://dudmail.com/freedom.txt)
* [https://www.jacobsparts.com/freedom.txt](https://www.jacobsparts.com/freedom.txt)
* [http://hoop-la.ca/freedom.txt](http://hoop-la.ca/freedom.txt)
* [http://kyleterry.com/freedom.txt](http://kyleterry.com/freedom.txt)
* [http://mvanveen.net/freedom.txt](http://mvanveen.net/freedom.txt)
* [http://jacobroufa.com/freedom.txt](http://jacobroufa.com/freedom.txt)
* [http://www.isingh.info/freedom.txt](http://www.isingh.info/freedom.txt)

[isingh]: http://www.isingh.info/blog/2012/01/22/support-an-open-internet-create-your-own-freedom-txt/trackback/
[freedomtxt]: http://mvanveen.net/freedom.txt

