import requests
from bs4 import BeautifulSoup
import re
from api.models import Quake

url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
raw = soup.pre.text
pattern = re.compile(
    r'\d{4}\.\d{2}\.\d{2}\s+\d{2}:\d{2}:\d{2}\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+-.-\s+['
    r'\d.]+\s+-.-\s+\S+(?:\s\S+)*?\s') 
matches = pattern.findall(raw)
for match in (matches):
    res = match.split()
    print(res)
    if not Quake.objects.filter(date=res[0], time=res[1]).exists():
        quake = Quake.objects.create(
            date=res[0],
            time=res[1],
            latitude=res[2],
            longitude=res[3],
            depth=res[4],
            md=res[5],  # Correctly assign the value to md
            ml=res[6], 
            mw=res[7],
            location=res[8],  # Assign the combined location
        )
        print("Saving the quake...")
        quake.save()