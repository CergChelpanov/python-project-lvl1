# Makefile

install: # установить зависимости
	poetry install
	poetry add prompt

build:
	poetry build

publish: 
	poetry publish --dry -run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

init: #подключить линтер flake8
	poetry run flake8 brain_games

start: #запустить приложение
	poetry run brain-games

