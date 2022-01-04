#! /usr/bin/env python3
"""
Author : Md. Nur Habib
GitHub     : https://github.com/thenurhabib
Facebook   : https://web.facebook.com/thenurhab1b 
HackerRank : https://www.hackerrank.com/thenurhabib
"""

# Import Modules
import requests, os
from time import sleep
from getpass import getpass

# Variables
lines = "-" * 44
userpass = ["cluric@user", "cluric@pass"]
headers = {
    "User-Agent": "Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"
}

# Colors
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
d = "\033[2;37m"
w = "\033[0m"

# Banner
def banner():
    print(
        f"""{b}
                    
                ╔═══╦╗──╔╗─╔╦═══╦══╦═══╗
                ║╔═╗║║──║║─║║╔═╗╠╣╠╣╔═╗║
                ║║─╚╣║──║║─║║╚═╝║║║║║─╚╝
                ║║─╔╣║─╔╣║─║║╔╗╔╝║║║║─╔╗
                ║╚═╝║╚═╝║╚═╝║║║╚╦╣╠╣╚═╝║
                ╚═══╩═══╩═══╩╝╚═╩══╩═══╝
                {d}Username Checker Tools{w}
                {d}Author : {w}{r}Md. Nur Habib{w}
               
    {y} GitHub     : https://github.com/thenurhabib
     Facebook   : https://web.facebook.com/thenurhab1b 
     HackerRank : https://www.hackerrank.com/thenurhabib {y}
               
               """
    )


banner()

# login
getusername = input(f"{g}Enter Username : ")
getpassword = getpass("Enter Password : ")
if getusername == userpass[0] and getpassword == userpass[1]:
    print(f"Login Successfully{g}")
    os.system("clear")
    print("\nYou Have successfully logged in, Loading Please Wait...")
    sleep(2)
    banner()
    username = str(input(f"{w}{b}>{w} enter username:{b} "))
    if not username:
        menu()
    urllist = [
        "https://facebook.com/{}",
        "https://instagram.com/{}",
        "https://twitter.com/{}",
        "https://youtube.com/{}",
        "https://vimeo.com/{}",
        "https://github.com/{}",
        "https://plus.google.com/{}",
        "https://pinterest.com/{}",
        "https://flickr.com/people/{}",
        "https://vk.com/{}",
        "https://about.me/{}",
        "https://disqus.com/{}",
        "https://bitbucket.org/{}",
        "https://flipboard.com/@{}",
        "https://medium.com/@{}",
        "https://hackerone.com/{}",
        "https://keybase.io/{}",
        "https://buzzfeed.com/{}",
        "https://slideshare.net/{}",
        "https://mixcloud.com/{}",
        "https://soundcloud.com/{}",
        "https://badoo.com/en/{}",
        "https://imgur.com/user/{}",
        "https://open.spotify.com/user/{}",
        "https://pastebin.com/u/{}",
        "https://wattpad.com/user/{}",
        "https://canva.com/{}",
        "https://codecademy.com/{}",
        "https://last.fm/user/{}",
        "https://blip.fm/{}",
        "https://dribbble.com/{}",
        "https://en.gravatar.com/{}",
        "https://foursquare.com/{}",
        "https://creativemarket.com/{}",
        "https://ello.co/{}",
        "https://cash.me/{}",
        "https://angel.co/{}",
        "https://500px.com/{}",
        "https://houzz.com/user/{}",
        "https://tripadvisor.com/members/{}",
        "https://kongregate.com/accounts/{}",
        "https://{}.blogspot.com/",
        "https://{}.tumblr.com/",
        "https://{}.wordpress.com/",
        "https://{}.devianart.com/",
        "https://{}.slack.com/",
        "https://{}.livejournal.com/",
        "https://{}.newgrounds.com/",
        "https://{}.hubpages.com",
        "https://{}.contently.com",
        "https://steamcommunity.com/id/{}",
        "https://www.wikipedia.org/wiki/User:{}",
        "https://www.freelancer.com/u/{}",
        "https://www.dailymotion.com/{}",
        "https://www.etsy.com/shop/{}",
        "https://www.scribd.com/{}",
        "https://www.patreon.com/{}",
        "https://www.behance.net/{}",
        "https://www.goodreads.com/{}",
        "https://www.gumroad.com/{}",
        "https://www.instructables.com/member/{}",
        "https://www.codementor.io/{}",
        "https://www.reverbnation.com/{}",
        "https://www.designspiration.net/{}",
        "https://www.bandcamp.com/{}",
        "https://www.colourlovers.com/love/{}",
        "https://www.ifttt.com/p/{}",
        "https://www.trakt.tv/users/{}",
        "https://www.okcupid.com/profile/{}",
        "https://www.trip.skyscanner.com/user/{}",
        "http://www.zone-h.org/archive/notifier={}",
        "https:www//codepen.io/{}",
        "https://www.hackerrank.com/{}",
        "https://dev.to/{}",
    ]
    print(w + lines)
    for url in urllist:
        try:
            req = requests.get(url.format(username), headers=headers)
            if req.status_code == 200:
                color = g
            elif req.status_code == 404:
                color = r
            else:
                color = y
            print(f"{b}[{color}{req.status_code}{b}] {w}{url.format(username)}")
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.TooManyRedirects:
            break
        except requests.exceptions.ConnectionError:
            break
else:
    print(f"{r}Sorry You Entred Wrong Login Information.{r}")
    exit()