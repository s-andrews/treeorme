from google_images_download import google_images_download   
import json
from pathlib import Path
import os

response = google_images_download.googleimagesdownload() 

with open(Path(__file__).parent / "search_terms.json") as st:
    arguments = json.load(st)


for record in arguments["Records"]:
    output_folder = Path(__file__).parent / record["folder"]
    del record["folder"]
    paths = response.download(record)
    
    for path in list(paths[0].values())[0]:
        file=path.split("\\")[-1]
        os.rename(path,str(output_folder / file))