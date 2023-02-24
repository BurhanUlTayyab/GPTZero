install:
	pip install --upgrade pip && pip install -r requirements.txt
format: 
	black *.py
lint:
	pylint --disable=R,C infer.py local_infer.py
