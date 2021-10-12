# Makefile

install: # установить зависимости
	poetry install

start: #запустить приложение
	poetry run brain-games

