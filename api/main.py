# Python
from routes import get_max_duration, get_score_count, get_count_platform, get_actor
# from models.predict_model import generate_recomendation
from models.predict_model import generate_recomendation

# FasAPI
from fastapi import FastAPI
from fastapi import Body # Para especificar que es body

app = FastAPI(
    docs_url="/",
    title="Lista de scores de películas/series",
    description="API desarrollado para entrenar un modelo de recomendación basado en el consumo de recursos en las plataformas Amazon Prime, Netflix, Hulu y Disney Plus de los usuarios.",
    version='0.0.1'
    )

# ------------------------------------------------------#
#                       POST                            #
# ------------------------------------------------------#


# ------------------------------------------------------#
#                           GET                         #
# ------------------------------------------------------#
# Request About
@app.get("/about")
async def about_me():
    pass


# Request 1
@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
async def pregunta_1(year: int,platform: str, duration_type: str):
    result = get_max_duration(year, platform, duration_type)
    return result

# # Request 2
@app.get('/get_score_count/{platform}/{score}/{year}')
async def pregunta_2(platform:str, score:int, year:int):
    result = get_score_count(platform, score, year)
    return result

# # Request 3
@app.get('/get_count_platform/{platform}')
async def pregunta_3(platform:str):
    result = get_count_platform(platform)
    return result

# # Request 4
@app.get('/get_actor/{platform}/{year}')
async def pregunta_4(platform:str,year:int):
    result = get_actor(platform,year)
    return result

# Prediccion del sistema de recomendación
@app.get('/model/predict/{user_id}/{top}')
async def predict_movie(user_id: int, top: int):
    result = generate_recomendation(user_id, top)
    return result