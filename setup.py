from setuptools import setup, find_packages

setup(
    name="Jogo_da_Velha", 
    version="0.1.0",  
    description="simulação de um jogo da velha",
    long_description=open("README.md").read(),
    license="MIT", 
    author="Malena Milani dos Santos",
    python_requires=">=3.8", 
    install_requires=['numpy','pandas'], 
    url= "https://github.com/Malena-yyy/modulo.git" ,
    packages=find_packages(), 

)
