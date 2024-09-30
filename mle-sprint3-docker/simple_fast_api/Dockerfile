FROM python:3.11-slim
LABEL author=${AUTHOR}

LABEL author="mle-student"
COPY . ./simple_fast_api
# директория simple_fast_api скопирована в Docker

WORKDIR simple_fast_api
# команды далее запускаются из этой директории

RUN pip3 install -r requirements.txt
# устанавливаем все зависимости

VOLUME /speeches
# говорим что папка является общим томом

EXPOSE ${APP_PORT}
#  прокидываем порт наружу, он же указан в команде запуска сервера
# если менять порт то сразу во всех местах
# это порт который используется внутри ОС контейнера
# запуская контейнер можно этот порт переопределить на другой - он и будет внешним портом для работы приложения
# EXAMPLE: docker container run --publish 4600:1702 simple_fast_api:2
# тут 4600 порт машины в которой запускается контейнер подменяет порт 1702 который крутится внутри образа

# docker container run --publish 4600:1702 --env-file .env --volume=./speeches:/simple_fast_api/speeches  simple_fast_api:with_env
# пример запуска с указанием env файла с параметрами среды и указанием куда должен обращаться том (VOLUME)


# укажем инструкцию по запуску микросервиса

CMD uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT}