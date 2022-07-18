build:
	pip3 install virtualenv
	virtualenv .
	cd bin && source activate
	python3 -m pip install Flask
	python3 -m pip install -U flask-cors

test-all:
	python3 -m unittest discover -s tests -p '*_test.py'

execute:
	export FLASK_APP=beaster_game_api.py; cd src; flask run --port=8080

run: build test-all execute

execute-mock:
	export FLASK_APP=mocked_beaster_game_api.py; cd mock; flask run --port=8080

execute-windows:
	$$env:FLASK_APP='beaster_game_api.py'; cd src; python -m flask run --port=8080

mock: build execute-mock
