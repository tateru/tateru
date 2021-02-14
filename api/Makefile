.PHONY: all

all: machine-service.api.html manager.api.html installer-boot.png

machine-service.api.html: machine-service.api.yaml
	\sudo rm -fr _temp
	docker run --rm -v $(PWD):/local/ -ti \
		swaggerapi/swagger-codegen-cli-v3:3.0.24 \
		generate -i /local/$^ -l html -o /local/_temp/
	cp _temp/index.html $@
	sudo rm -fr _temp

manager.api.html: manager.api.yaml
	\sudo rm -fr _temp
	docker run --rm -v $(PWD):/local/ -ti \
		swaggerapi/swagger-codegen-cli-v3:3.0.24 \
		generate -i /local/$^ -l html -o /local/_temp/
	cp _temp/index.html $@
	sudo rm -fr _temp

installer-boot.png: installer-boot.uml
	./uml.py < installer-boot.uml > installer-boot.png
