
FROM python:3.11-slim-bullseye

WORKDIR /streamlit
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . /streamlit

# Intentionally do not expose port 8501 or else people can circumvent login

COPY ./requirements.txt /streamlit/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /streamlit/requirements.txt

CMD streamlit run Home.py