# project id - replace with your GCP project id
PROJECT_ID=lewagon-bootcamp-310515

# bucket name - replace with your GCP bucket name
BUCKET_NAME=musicwithemotions

# choose your region from https://cloud.google.com/storage/docs/locations#available_locations
REGION=europe-west1

BUCKET_FOLDER = Data

LOCAL_PATH = /home/alexbabkf/code/AlexBabkf/MusicWithEmotions/raw_data/icml_face_data.csv

BUCKET_FILE_NAME = $(shell basename ${LOCAL_PATH})

PYTHON_VERSION=3.7
FRAMEWORK=scikit-learn
RUNTIME_VERSION=1.15

PACKAGE_NAME=MusicWithEmotions
FILENAME=modeltest

JOB_NAME=first_training_$(shell date +'%Y%m%d_%H%M%S')

set_project:
	@gcloud config set project ${PROJECT_ID}

create_bucket:
	@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

upload_data:
	@gsutil cp ${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${BUCKET_FILE_NAME}

# GCP TRAINING

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
  		--job-dir gs://${BUCKET_NAME}/${BUCKET_TRAINING_FOLDER}	\
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION} \
		--stream-logs

# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* MusicWithEmotions/*.py

black:
	@black scripts/* MusicWithEmotions/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr MusicWithEmotions-*.dist-info
	@rm -fr MusicWithEmotions.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)


