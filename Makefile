build:
	docker build -t checkout_image .
run:
	docker run -dp=5000:5000 --name=checkout_image checkout_image

up: build run
stop:
	docker stop checkout_image
