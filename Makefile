setup:
	python3 -m venv .venv
install:
	pip install -r .\requirements.txt
pylint: 
	pylint --generate-rcfile > .pylintrc
