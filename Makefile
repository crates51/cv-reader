build:
	docker-compose build

up:
	echo "Bringing up the project..."
	make down
	docker-compose up --abort-on-container-exit

down:
	docker-compose down -v

connect_main:
	docker-compose exec cv_reader bash

connect_main_root:
	docker-compose exec -u root cv_reader bash
