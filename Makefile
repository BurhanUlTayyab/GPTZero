install:
	pip install --upgrade pip && pip install -r requirements.txt
format: 
	black *.py
lint:
	pylint --disable=R,C --generated-members exp stack *.py
