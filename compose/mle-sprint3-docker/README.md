# mle-sprint3
Репозиторий с авторским решением третьего спринта

docker image build . --tag lesson6:final
docker container run --publish 4601:8081 --volume=./models:/churn_app/models  --env-file .env lesson6:final