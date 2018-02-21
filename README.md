(WIP)

### Netflix migrator

A python script to move netflix data from one account to another.


#### Use

(clone repo)


To save titles of a profile,

1. Go to https://www.netflix.com/YourAccount
2. Export your cookies.txt with a browser extention ([chrome](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg), [firefox](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/))
3. place cookies.txt in the root of this project
4. install all requirements with `pip install -r requirements.txt`
4. run the script with `python save.py` 

#### Disclaimer

While it's possible to bring your recommendation over, you should NOT use this for "unlimited free netflix" and it is not intended for this.


#### TODO

Need to impliment importing data. Currently only exports titles, and that may break with large watch histories.