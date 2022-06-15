GIT_TAG := $(shell git describe --abbrev=0 --tags)

install-python-env:
	pipenv sync

gen-dev-env-variable:
	python genenv.py

gen-staging-env-variable:
	VERSION=STAGING python genenv.py

gen-release-env-variable:
	VERSION=RELEASE python genenv.py

build-image:
	docker build -f Dockerfile -t louisekr/api:${GIT_TAG} .

up-api:
	docker-compose -f api.yml up

tag-image:
	docker tag api:1.0.1 louisekr/api:1.0.1

push-image:
	docker push louisekr/api:${GIT_TAG}

deploy-api:
	GIT_TAG=${GIT_TAG} docker stack deploy --with-registry-auth -c api.yml api