import scraper_helper as sh

BOT_NAME = "amazon"

SPIDER_MODULES = ["amazon.spiders"]
NEWSPIDER_MODULE = "amazon.spiders"



ROBOTSTXT_OBEY = False
AUTOTHROTTLE_ENABLED = True



DEFAULT_REQUEST_HEADERS = sh.get_dict(

'''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
cookie: session-id=260-5874485-2760255; i18n-prefs=EUR; lc-acbde=en_GB; ubid-acbde=257-6233833-2244109; session-id-time=2082787201l; sp-cdn="L5Z9:PK"; session-token=JawI4Csh+Bb+eaIJfj0pL6AXmYwQ2WTm0s+ilcPlrp58lEQOQVxOby59cE0shPCvMiDrCUW/HhWAm7DTbSq6DjgtPkuRCM51JPWu89+4q1pKKMSmxqPMSjB24UYKM/pxpbfAAPE5qlEVPixO6cVYUJ/+MPBveDXfgMWtvZDYxCNGFI24doRY/citS4XQttraP2BCOFa+KDVf4rSrM6IsbwbNaVdUEdn80KgWqg7y1sE=; csm-hit=adb:adblk_yes&t:1676301979710&tb:RM95JDX1D6BMJ5VVB64K+s-FQANRVR2GZFDSBAX1HBN|1676301979710
device-memory: 8
downlink: 1.45
dpr: 1
ect: 3g
rtt: 300
sec-ch-device-memory: 8
sec-ch-dpr: 1
sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-ch-ua-platform-version: "10.0.0"
sec-ch-viewport-width: 653
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36
viewport-width: 653
'''
)

