
venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv -p python3.8 venv
	. venv/bin/activate; pip install --no-cache-dir -Ur requirements.txt
	touch venv/bin/activate

clean:
	rm -rf venv
	rm -rf .vscode/
	find -iname "*.pyc" -delete



run:
	export FLASK_APP="flaskblog.py" && \
	. venv/bin/activate && flask run 