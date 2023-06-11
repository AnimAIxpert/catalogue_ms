# import sys
import pandas as pd
# sys.path.append('..')
from .models import Anime


def load_base_data(db_session):
    try:
        data = pd.read_csv("data/anime.csv")
        # print(data)
        # anime = data.iloc[0]
        for ind, anime in data.iterrows():
            temp = Anime()
            if anime["MAL_ID"] != "Unknown":
                temp.id = anime["MAL_ID"]
            temp.name = anime["Name"]
            if anime["Score"] == "Unknown":
                temp.score = 0
            else: 
                temp.score = anime["Score"]
            temp.genres = anime["Genres"]
            temp.english_name = anime["English name"]
            temp.japanese_name = anime["Japanese name"]
            temp.type = anime["Type"]
            if anime["Episodes"] == "Unknown":
                temp.episodes = 0
            else:
                temp.episodes = anime["Episodes"]
            temp.aired = anime["Aired"]
            temp.premiered = anime["Premiered"]
            temp.producers = anime["Producers"]
            temp.licensors = anime["Licensors"]
            temp.studios = anime["Studios"]
            temp.source = anime["Source"]
            temp.duration = anime["Duration"]
            temp.audience = anime["Rating"]
            db_session.add(temp)
        db_session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def load_sypnosis(db_session):
    try:
        dataframe = pd.read_csv("data/anime_with_synopsis.csv")
        # print(dataframe['synopsis'][0])
        for ind, anime in dataframe.iterrows():
            register = db_session.query(Anime).filter(Anime.id == anime["MAL_ID"]).first()
            register.synopsis = anime["synopsis"]
        db_session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def load_images_path(db_session):
    try:
        dataframe = pd.read_csv("data/images_paths.csv")
        for ind, anime in dataframe.iterrows():
            register = db_session.query(Anime).filter(Anime.id == anime["MAL_ID"]).first()
            register.image_url = anime["image_url"]
        db_session.commit()
        return True
    
    except Exception as e:
        print(e)
        return False

# if __name__ == "__main__":
#     try:
#         q = db_session.query(Anime).all()
#         if len(q) == 0:
#             print("Loading database...")
#             load_base_data()
#             load_sypnosis()
#             load_images_path()
#             print("Database loaded")
#     except Exception as e:
#         print("Error loading database: ", e)

