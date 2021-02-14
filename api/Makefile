# Copyright 2021 Tateru Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
