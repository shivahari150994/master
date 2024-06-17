from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Shivahari Revathi Venkateswaran',
    author_email='venkateswaranshivahari@gmail.com',
    install_requires=["openai", "langchain==0.1.6", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)