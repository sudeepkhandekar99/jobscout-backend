Setup Python:
venv\Scripts\activate
pip install -r requirements.txt

Setup DB:
create database jobscout;
CREATE USER jobscout_user WITH PASSWORD 'root';
GRANT ALL PRIVILEGES ON DATABASE jobscout TO jobscout_user;

Run Backend:
uvicorn app.main:app --reload