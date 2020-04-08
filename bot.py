import cloudscraper
import time
import threading
from bs4 import BeautifulSoup
from config import *


class Autoclaim(threading.Thread):
    def __init__(self, site, delay):
        threading.Thread.__init__(self)
        self.site = site
        self.delay = delay
        
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }    
        scraper = cloudscraper.CloudScraper()
        while True:
            try:
                conn_ = scraper.post(self.site, headers=headers)
            except Exception as e:
                print(e)
            soup = BeautifulSoup(conn_.text, "html.parser")
            if conn_.status_code == 200:
                try:
                    name = soup.title
                    print(name.string + "  " + "Success Claim")
                except Exception:
                    print(self.site + "  " + "Success Claim")
            else:
                try:
                    name = soup.title
                    print(name.string + "  " + "Fail Claim")
                except Exception:
                    print(self.site + "  " + "Fail Claim")
            time.sleep(self.delay)

#main
fix_site = ["http://dutchybig.ovh/faucet.php?r=EC-UserId-26314&rc=DOGE&address="+user+"&currency=DOGE&key="+ dutchybig_key ,
        "https://www.auto.anonymousfaucet.xyz/faucet.php?r=EC-UserId-26314&rc=DOGE&address=" + user + "&currency=DOGE&key=" + anonymousfaucet_key ,
        "http://ecauto.japakar.com/faucet.php?r=EC-UserId-26314&rc=DOGE&address=" + user + "&currency=DOGE&miner=on&key=" + ecauto_key ]
for x in range(len(fix_site)):
    temp = Autoclaim(site = fix_site[x], delay = 60)
    temp.start()
