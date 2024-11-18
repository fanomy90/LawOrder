FROM python:3.11.2

SHELL ["/bin/bash", "-c"]
# Настройки виртуального окружения: запрет создания кэш файлов и запрет буферизации сообщений с логами 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y curl && apt-get clean
WORKDIR /yt
COPY ./requirements.txt /yt/
# Установим зависимости проекта
RUN pip install -r requirements.txt
COPY ./LawOrder /yt/
RUN chmod +x /yt/LawOrderBot/LawOrderBot.py