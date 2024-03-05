local-down-app:
	docker-compose --env-file ./deploy/env/.env.local -f docker-compose.local.yaml down -v

local-start-app:
	docker-compose --env-file ./deploy/env/.env.local -f docker-compose.local.yaml up -d --build

init-alembic:
	alembic init migrations

create-migration:
	alembic revision -m "${name}"

local-migration-up:
	alembic -x env_path="./deploy/env/.env.local" upgrade head

local-migration-base:
	alembic -x env_path="./deploy/env/.env.local" downgrade base

local-start-weather-app:
	python main.py --env="deploy/env/.env.local"