from google_images_download import google_images_download   
import json
from pathlib import Path

response = google_images_download.googleimagesdownload() 

with open(Path(__file__).parent / "search_terms.json") as st:
    arguments = json.load(st)

print(arguments)

for record in arguments["Records"]:
    paths = response.download(record) 
    print(paths)