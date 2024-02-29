pip install virtualenv

python3 -m virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cat .env-example > .env

uvicorn app.main:app --reload
