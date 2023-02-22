<h1 align="center">Proyecto Individual 01 - MLOps para un Sistema de Recomendación en una Startup de Agregación de Plataformas de Streaming</h1>

<p align="center">
Solución de problemas de modelos de recomendación en un entorno de streaming, desde la transformación de datos hasta el mantenimiento del modelo. Desarrollo de un MVP como Data Scientist en una start-up de agregación de plataformas de streaming.
</p>


<h2 align="center"><b>Sistema de recomendación basado en Filtrado Colaborativo</b></h2>

<p align="justify">
Este es un proyecto de MLOps para implementar un sistema de recomendación en una startup de agregación de plataformas de streaming. Como Data Scientist en la empresa, se enfrenta al desafío de crear un sistema de recomendación efectivo desde cero, y en un plazo muy ajustado.
</p>

<h2 align='center'>Descripción del Problema</h2>

<p align="justify">
La empresa proporciona servicios de agregación de plataformas de streaming. El objetivo es crear un sistema de recomendación que permita a los usuarios encontrar contenido relevante y personalizado. Los datos actuales de la empresa son insuficientes y no están procesados, lo que hace que el trabajo de un Data Scientist sea imposible.
</p>
<p align="justify">
El proyecto tiene como objetivo construir una solución de MLOps que resuelva el problema y permita a la empresa ofrecer recomendaciones personalizadas a sus usuarios.
</p>

<h2 align='center'>Rol a Desarrollar</h2>

En este proyecto, el rol a desarrollar es el de Data Scientist. El objetivo es desarrollar un sistema de recomendación utilizando técnicas de Machine Learning. También se debe hacer el trabajo de un Data Engineer, procesando y transformando los datos para prepararlos para su uso en el modelo de ML. Además, se debe implementar un sistema de MLOps para automatizar el proceso de entrenamiento y despliegue del modelo.

<h2 align="center">Solución Propuesta</h2>

<p align="justify">
Para abordar el problema, se propone un enfoque de MLOps que contemple las siguientes etapas:
</p>

1. **Recopilación y procesamiento de datos:** Se recopilarán los datos de las diferentes plataformas de streaming y se procesarán para prepararlos para su uso en el modelo de recomendación. Esto incluye la eliminación de datos faltantes, la transformación de datos y la creación de nuevas características.

2. **Desarrollo del modelo de recomendación:** Se desarrollará un modelo de recomendación utilizando técnicas de Machine Learning como la Factorización de Matrices. El modelo se entrenará utilizando los datos procesados y se evaluará su rendimiento.

3. **Implementación del modelo en producción:** Se implementará el modelo en producción utilizando un sistema de MLOps que automatice el proceso de entrenamiento y despliegue. Se utilizará un contenedor Docker para empaquetar el modelo y se desplegará en un servidor web.

4. **Monitoreo y mantenimiento del modelo:** Se realizará un monitoreo continuo del modelo en producción para asegurarse de que esté funcionando correctamente. También se implementarán estrategias de mantenimiento para actualizar y mejorar el modelo a medida que se recopilan nuevos datos.

<h2 align="center">Tecnologías Utilizadas</h2>

Para implementar la solución propuesta, se utilizarán las siguientes tecnologías:

- [x] Python: para el desarrollo del modelo de recomendación y el procesamiento de datos.
- [x] Pandas y Numpy: para la manipulación de datos.
- [x] scikit-surprise o surprise: para el desarrollo del modelo de recomendación basado en el filtro colaborativo.
- [ ] Docker: para el empaquetamiento y despliegue del modelo en producción.
- [x] FastAPI: para el desarrollo de la API.
- [ ] Cloud Run: para desplegar nuestra API o [Deta Space](https://deta.space/).
- [x] GitHub: para el control: de versiones del código.
- [ ] GitHub Actions: Para controlar y activar los tres workflows el primero de testing, el segundo de CI/CD (Continuos Integracion Continuos Deployment) y el entrenamiento continuo que va utitilizar Surprise, Data Version Control (DVC) y Continuos Machine Learning (CML).
- [ ] DVC: Para serializar a través de hashes nuestros datos conectando con Google Cloud Storage guardando nuetro dataset y modelo entrenado.
- [ ] GCP: para el alojamiento del modelo en producción.
- [x] Gradio: para desarrollar la interfaz de la demo del proyecto.

<h2>Demostración del Proyecto</h2>

Para acceder a la API desarrollada y desplegada en Deta Space verifique [aquí](https://deta.space/discovery/r/j7anjobxgmaeplkf) para poder probar la API deve crearse una cuenta en [Deta Space](https://deta.space/login) y posteriormente instalar en Space.

Para probar el funcionamiento del Modelo de Sistema de Recomendación en Hugging Face [aquí](https://huggingface.co/spaces/royquilca/recommender_system_pi)

<h2>Conclusiones</h2>

<p align="justify">
Este proyecto de MLOps permitirá a la empresa proporcionar recomendaciones personalizadas a sus usuarios, mejorando así la experiencia del usuario y aumentando la retención de clientes. La implementación de un sistema de MLOps también permitirá a la empresa automatizar el proceso de entrenamiento y despliegue del modelo, lo que reducirá el tiempo de desarrollo y mejorará la eficiencia del equipo de Data Science.
</p>
<p align="justify">
En resumen, este proyecto de MLOps es un ejemplo práctico de cómo abordar un problema de Machine Learning en una startup. Al utilizar tecnologías modernas y buenas prácticas de desarrollo, se puede lograr un sistema de recomendación efectivo que beneficie tanto a la empresa como a sus usuarios.
</p>


---

<h2>Installation guide</h2>

Para revisar los más detalles de configuración de este proyecto por favor revise [installation.md](installation.md).

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description
    │   └── models              <- Notebooks of Machine learning or Deep Learning models.
    │   └── feature_engineering <- Notebooks of cleaning, transforming data, export final dataset.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so src can be imported.
    │
    └── src               <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---
Project based on the [cookiecutter-ds](https://github.com/royquillca/cookiecutter-ds).