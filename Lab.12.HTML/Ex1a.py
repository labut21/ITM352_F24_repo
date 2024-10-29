import urllib.request
import ssl

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"


ssl._create_default_https_context = ssl._create_unverified_context
web_page = urllib.request.urlopen(url)

print(web_page)