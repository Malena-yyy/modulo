from setuptools import setup, find_packages

setup(
    name='Jogo_da_velha',
    version='0.1.0',
    description='Simulação de um jogo da velha',
    author='Malena Milani dos Santos',
    python_requires='>=3.6',
    install_requires=['numpy','random'],
    packages=find_packages(),
)