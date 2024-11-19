# Docker
run_mongodb_docker_with_auth:
	docker run -d -p 27017:27017 --name mongodb \
	-e MONGO_INITDB_ROOT_USERNAME=admin \
	-e MONGO_INITDB_ROOT_PASSWORD=password \
	mongo:7.0

run_mongodb_docker:
	docker run -d -p 27017:27017 --name mongodb \
	mongo:7.0

# APIs
insert_mock_application:
	curl -X POST "http://localhost:8000/applications" -H "Content-Type: application/json" \
	-d '{"job_title": "Software Engineer", "company": "OpenAI", "date_applied": "2024-11-17"}'