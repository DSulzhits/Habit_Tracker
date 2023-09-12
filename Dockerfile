# Poetry container
FROM python:3

WORKDIR /code

COPY . .

COPY ./poetry.lock /code/

COPY ./pyproject.toml /code/

RUN pip install 'poetry==1.6.1'

RUN poetry config virtualenvs.create false

RUN poetry install --no-root


## Venv container
#FROM python:3
#
#WORKDIR /code
#
#COPY ./requirements.txt /code/
#
#RUN pip install -r requirements.txt
#
#COPY . .
