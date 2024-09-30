Микросервис для запуска ML-модели 

Пример запуска из директории mle-sprint3-docker:

uvicorn app.churn_app:app --reload --port 8081 --host 0.0.0.0
Для просмотра документации API и совершения тестовых запросов зайти на  http://127.0.0.1:8081/docs


Если используется другой порт, то заменить 8081 на этот порт

Сборка и запуск контейнера

docker image build . --tag churn_app:2
docker container run --publish 4601:1702 --volume=./models:/churn_app/models   --env-file .env churn_app:2