import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.
    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.
    Args:
        nothing
    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='src',
    version='0.1.0',
    author='Roy Quillca',
    author_email='royquillca@outlook.es',
    description='Solución de problemas de modelos de recomendación en un entorno de streaming, desde la transformación de datos hasta el mantenimiento del modelo. Desarrollo de un MVP como Data Scientist en una start-up de agregación de plataformas de streaming.',
    python_requires='>=3',
    license="MIT",
    url='',
    packages=find_packages(),
    long_description=readme()
)