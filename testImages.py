import httpx
import re
import pandas as pd
from tqdm import tqdm
import time

data = pd.read_csv("data/anime.csv")
regex_string = "https://cdn.myanimelist.net/images/anime/[0-9]*/[0-9]*.jpg"
paths_file_path = "data/images_paths1.csv" 
ids_list = list(data['MAL_ID'])

print(ids_list[4882+151])

# try:
#     for anime_id in tqdm(ids_list[6000:7200]):
#         res = httpx.get(f"https://myanimelist.net/anime/{anime_id}/")
#         if res.status_code == 404:
#             print(f"Anime {anime_id} not found, skiping...")
#             continue
#         if res.status_code == 429:
#             print(f"se putio en {anime_id}")
#             time.sleep(60*5)
#             continue
#         string = res.read().decode("utf-8")
#         match = re.search(regex_string, string).group()
#         with open(paths_file_path, "a") as f:
#             f.write(f"{anime_id},\"{match}\"\n")
# except Exception as e:
#     print(e)