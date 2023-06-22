Python program to get text of a CV, send it to chat.openAI to return a sintesis to dowload as pdf.

Setting up All dependencies of this project are dealt by poetry. In order to retrieve all necessary dependencies, you need to:

Install poetry: https://python-poetry.org/docs/#installation
Run :

$poetry shell (to activate virtual environment) $poetry install (to install dependencies)

Create openai API key :

here the doc : https://platform.openai.com/docs/api-reference

Create your .env replacing "your api key" by your effective API key

Run project

$python3 app.py
