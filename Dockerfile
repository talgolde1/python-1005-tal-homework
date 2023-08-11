
FROM python:3.9
WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY Scores/Scores.txt /app/Scores.txt
EXPOSE 8777
CMD ["python", "MainGame.py"]
