install:
	pip install -r requirements.txt

run-local:
	uvicorn app.main:app1 --reload