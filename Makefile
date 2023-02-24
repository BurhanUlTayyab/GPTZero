install:
	pip install --upgrade pip && pip install -r requirements.txt
format: 
	black *.py
lint:
	pylint --disable=R,C --extension-pkg-whitelist=torch *.py
