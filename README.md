# Cherre_Assignement

The project utilizes SQLite 3 with Python3 hosted on a Flask server. 

## Running Locally

Running the project is as simple as running the main in app.py but first we need to install Flask:
```bash
pip install flask
python app.py
```
You should see
```
 * Restarting with stat
 * Debugger is active!
 ```

## Using PostMan

To see the api working, go over to Postman after running the flask server locally.
The POST request will take the following URL:
```bash
http://localhost:5000/freqUser
```
This will hit the freqUser endpoint that queries the frequent_browser database table. It will return the result in the following format:
```bash
FirstName|PersonID|Count(Visits)
```
