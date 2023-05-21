import httpx
import re
import pandas as pd
from tqdm import tqdm

data = pd.read_csv("data/anime.csv")
regex_string = "https://cdn.myanimelist.net/images/anime/[0-9]*/[0-9]*.jpg"
paths_file_path = "data/images_paths.csv" 
ids_list = list(data['MAL_ID'])

try:
    for anime_id in tqdm(ids_list):
        res = httpx.get(f"https://myanimelist.net/anime/{anime_id}/")
        if res.status_code != 200:
            print(f"Error getting anime {anime_id}")
        string = res.read().decode("utf-8")
        match = re.search(regex_string, string).group()
        with open(paths_file_path, "a") as f:
            f.write(f"{anime_id},\"{match}\"\n")
except Exception as e:
    print(e)