build:
	pip3 install virtualenv
	virtualenv .
	cd bin && source activate
	Python3 -m pip install Flask

execute:
	export FLASK_APP=game_api.py; cd ./src/controller; flask run --port=8080

run: build execute

mock: build
	export FLASK_APP=mocked_game_api.py; cd ./mock; flask run --port=8080