Python program to get text of a CV, send it to chat.openAI to return a sintesis to dowload as pdf.

**Setting up**
All dependencies of this project are dealt by pip.
In order to retrieve all necessary dependencies, you need to:

- Install virtual env

  > > $ pip install virtualenv

- Activate venv :

# On Windows

> > $source env/Scripts/activate

(env) indicate that your env is activated

# On Linux

> > $ source env/bin/activate

- Install all dependencies :

> > $pip install -r requirements.txt

- Configure your .env :

create your env file (from .env_EXEMPLE) with port and server adress

- Create openai API key :

here the doc : https://platform.openai.com/docs/api-reference

- Create your .env replacing "your api key" by your effective API key
  you can configure port and host too.

**Run project**

> > $python3 app.py
