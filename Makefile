install-python-env:
	pipenv sync

gen-dev-env-variable:
	python genenv.py

gen-staging-env-variable:
	VERSION=STAGING python genenv.py

gen-release-env-variable:
	VERSION=RELEASE python genenv.py

build-image:
	docker build -f Dockerfile -t api:1.0.1 .

up-api:
	docker-compose -f api.yml up

tag-image:
	docker tag api:1.0.1 louisekr/api:1.0.1

push-image:
	docker push louisekr/api:1.0.1