**Backend Programming Exercise**

Please follow the following steps to run the application

* Create a virtual enviroment

  ```
  python -m venv venv
  ```
  ```
  source venv/bin/activate
  ```
* Install required packages

  ```
  pip install -r requirements.txt
  ```
* Download the .env file from the following drive and add it to the root project

  ```
  https://drive.google.com/file/d/1FNoz0NS3ZCVqlU9s3Ta00YqTOeusZdv5/view?usp=sharing
  ```
* Run the flask application locally on port 8000

  ```
  gunicorn --reload --bind 127.0.0.1:8000 app:app
  ```
* Make sample request provided on the exercise

  ```
  curl --location --request PUT 'http://127.0.0.1:8000/users' \
    --header 'Content-Type: application/json' \
    --data '{
        "user_id": "66b3d17ce6d8e2f5b93324d3", 
        "first_name" : "Jorge I",
        "password" : "billmd124Pass$",
        "updated_datetime" : "2024-08-07T22:26:12.111Z"
    }'
  ```
