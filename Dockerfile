FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY . .
EXPOSE 8081

# 默认命令 (会被 docker-compose.yml 中的 command 覆盖)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
