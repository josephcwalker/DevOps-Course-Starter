FROM python:3-alpine AS base

WORKDIR /opt/app

# Install Poetry
RUN pip install pipx && \
    pipx install poetry && \
    ln -s ~/.local/bin/poetry /usr/bin/poetry

# Install Dependencies
COPY ./poetry.lock ./pyproject.toml ./poetry.toml ./
RUN poetry install

# Copy App
COPY ./todo_app/ ./todo_app/


FROM base AS prod

ENV FLASK_DEBUG=false

CMD [ "poetry", "run", "gunicorn", "--bind=0.0.0.0:5000", "todo_app.app:create_app()" ]
EXPOSE 5000


FROM base AS dev

ENV FLASK_APP=todo_app/app

CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000" ]
EXPOSE 5000
