FROM amd64/python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader punkt

COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "translate.py"]

