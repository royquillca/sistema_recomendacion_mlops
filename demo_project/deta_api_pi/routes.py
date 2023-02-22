# Importacion de librerías
import pandas as pd
import numpy as np
from itertools import chain
from collections import Counter


# movies_scores_df = pd.read_parquet("api_data.parquet")
movies_scores_df = pd.read_csv("api_data.csv")

def get_max_duration(year: int,platform: str, duration_type: str):
    mask_year = movies_scores_df["release_year"] == year
    mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
    mask_duration_type = movies_scores_df['duration_type'] == duration_type
    mask_movie_type = movies_scores_df['type'] == 'movie'
    result = movies_scores_df[mask_year&mask_platform&mask_duration_type&mask_movie_type].sort_values(by='duration_int', ascending=False).iloc[0]
    return {
        'title': result.title,
        'platform': platform,
        'duration_type': duration_type,
        'duration_int': int(result.duration_int),
        'year': year,
    }
# La duracion máxima de una película en la plataforma hulu publicado en el año 2010
# print(get_max_duration(2010,'hulu','min'))


def get_score_count(platform: str, score: float, year: int):
    mask_movie_type = movies_scores_df['type'] == 'movie'
    mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
    mask_more_than_score = movies_scores_df['score'] > score
    mask_year = movies_scores_df['release_year'] == year
    count = movies_scores_df[mask_movie_type&mask_platform&mask_more_than_score&mask_year].shape[0]
    return {
        'platform': platform, 
        'score': score,
        'year': year,
        'count': count
    }
# Cantidad de películas que tieien un score mayor a 0.5 que fueron lanzadas en el 2010 en la plataforma netflix
# print(get_score_count('netflix',0.5,2010))

def get_count_platform(platform: str):
    mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
    count = movies_scores_df[mask_platform].shape[0]
    return {
        "platform": platform,
        "count": count
    }
# Cantidad de películas en la plataforma amazon
# print(get_count_platform('amazon'))


def get_actor(platform: str, year: int):
    mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
    mask_year = movies_scores_df["release_year"] == year
    cast_list = movies_scores_df[mask_platform&mask_year]['cast'].apply(lambda x: str(x).split(', '))
    actors = list(chain.from_iterable(cast_list))
    actors = list(map(str.strip, actors))
  
    actor_counts = Counter(actors)
    most_common_actor, count = actor_counts.most_common(1)[0]
    return {
        "platform": platform,
        "most_common_actor": most_common_actor,
        "count": count
    }

# def get_actor(platform: str, year: int, none_val=""):
#     mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
#     mask_year = movies_scores_df["release_year"] == year
#     cast_list = movies_scores_df[mask_platform&mask_year]['cast'].apply(lambda x: str(x).split(', '))
#     actors = list(chain.from_iterable(cast_list))
#     actors = list(map(str.strip, actors))
#     if none_val == "":    
#         actor_counts = Counter(actors)
#         most_common_actor, count = actor_counts.most_common(1)[0]
#         return {
#             "platform": platform,
#             "most_common_actor": most_common_actor,
#             "count": count
#         }
#     elif none_val == "not_none":
#         actors = list(filter(lambda x: x.lower() != "none", actors))
#         if len(actors) > 0:
#             actor_counts = Counter(actors)
#             most_common_actor, count = actor_counts.most_common(1)[0]
#             return {
#                 "platform": platform,
#                 "most_common_actor": most_common_actor,
#                 "count": count
#             }
#         else:
#             return {
#                 "platform": platform,
#                 "most_common_actor": "No existen valores no nulos",
#                 "count": 0
#             }


# Actor más popular (que más se repite) en la plataforma amazon durante el año 2010
# print(get_actor("amazon",2010))
