import pickle
import pandas as pd


def generate_recomendation(user_id, top=4):
    """
    Genera recomendaciones para un usuario utilizando el modelo SVD

    Args:
    - svd_model: modelo SVD previamente entrenado
    - user_id: id del usuario para el cual se generarán las recomendaciones
    - top: cantidad de recomendaciones a generar (default=4)
    - df: DataFrame con columnas 'userId', 'movieId', 'score', 'title'

    Returns:
    - lista de títulos de películas recomendadas
    """
    
    # Cargamos el modelo entrenado
    fc_model_dir = "fc_model_svd_v1.pkl"
    with open(f'{fc_model_dir}', 'rb') as file:
        svd_model = pickle.load(file)
        
    # Cargamos el dataset para el modelo
    df = pd.read_parquet("fc_model.parquet")
    
    # Obtener las películas que el usuario no ha visto aún
    movies_seen = set(df[df['userId'] == user_id]['movieId'])
    movies_all = set(df['movieId'])
    movies_unseen = list(movies_all - movies_seen)

    # Obtener las recomendaciones
    predicted_ratings = [svd_model.predict(user_id, movie_id).est for movie_id in movies_unseen]

    # Ordenar las películas según su predicción de rating
    movie_rating = list(zip(movies_unseen, predicted_ratings))
    movie_rating.sort(key=lambda x: x[1], reverse=True)

    # Obtener los títulos de las películas recomendadas
    recommended_movies = movie_rating[:top]
    recommended_titles = [df[df['movieId'] == movie_id]['title'].iloc[0] for movie_id, _ in recommended_movies]

    return {
        "recommended_movies": [movie.title() for movie in recommended_titles],
        "user_id": user_id,
        "top": 3 
    }

# print(generate_recomendation(543,top=3))