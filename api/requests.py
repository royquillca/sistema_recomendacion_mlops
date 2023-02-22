# # Importacion de librerías
# import pandas as pd
# import numpy as np
# from itertools import chain
# from collections import Counter

# # Gestionar las rutas
# import utils.paths as path

# # api_data_dir = pyprojroot.here("dataset").joinpath("api_data.parquet")

# dataset_dir = path.make_dir_function("dataset")
# api_data_dir = dataset_dir("api_data.parquet")


# movies_scores_df = pd.read_parquet(api_data_dir)

# # movies_scores_df = pd.read_parquet("dataset/api_data.parquet")

# def get_max_duration(year: int,platform: str, duration_type: str):
#     mask_year = movies_scores_df["release_year"] == year
#     mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
#     mask_duration_type = movies_scores_df['duration_type'] == duration_type
#     mask_movie_type = movies_scores_df['type'] == 'movie'
#     result = movies_scores_df[mask_year&mask_platform&mask_duration_type&mask_movie_type].sort_values(by='duration_int', ascending=False).iloc[0]
#     return {
#         'title': result.title,
#         'platform': platform,
#         'duration_type': duration_type,
#         'duration_int': int(result.duration_int),
#         'year': year,
#     }
# # La duracion máxima de una película en la plataforma hulu publicado en el año 2010
# # print(get_max_duration(2010,'hulu','min'))


# def get_score_count(platform: str, score: float, year: int):
#     mask_movie_type = movies_scores_df['type'] == 'movie'
#     mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
#     mask_more_than_score = movies_scores_df['score'] > score
#     mask_year = movies_scores_df['release_year'] == year
#     count = movies_scores_df[mask_movie_type&mask_platform&mask_more_than_score&mask_year].shape[0]
#     return {
#         'platform': platform, 
#         'score': score,
#         'year': year,
#         'count': count
#     }
# # Cantidad de películas que tieien un score mayor a 0.5 que fueron lanzadas en el 2010 en la plataforma netflix
# # print(get_score_count('netflix',0.5,2010))

# def get_count_platform(platform: str):
#     mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
#     count = movies_scores_df[mask_platform].shape[0]
#     return {
#         "platform": platform,
#         "count": count
#     }
# # Cantidad de películas en la plataforma amazon
# # print(get_count_platform('amazon'))



# def get_actor(platform: str, year: int):
#     mask_platform = movies_scores_df['show_id'].str[0] == platform[0]
#     mask_year = movies_scores_df["release_year"] == year
#     cast_list = movies_scores_df[mask_platform&mask_year]['cast'].apply(lambda x: str(x).split(', '))
#     actors = list(chain.from_iterable(cast_list))
#     actors = list(map(str.strip, actors))
  
#     actor_counts = Counter(actors)
#     most_common_actor, count = actor_counts.most_common(1)[0]
#     return {
#         "platform": platform,
#         "most_common_actor": most_common_actor,
#         "count": count
#     }


# # Actor más popular (que más se repite) en la plataforma amazon durante el año 2010
# # print(get_actor("amazon",2010))

import pyprojroot
import pandas as pd

# data_dir = pyprojroot.here("dataset").joinpath("api_data.parquet")


print(pd.read_parquet(pyprojroot.here("dataset").joinpath("api_data.parquet")).columns)