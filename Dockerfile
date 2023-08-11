
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY Scores.txt /Scores.txt
EXPOSE 8777
CMD ["python", "MainGame.py"]
