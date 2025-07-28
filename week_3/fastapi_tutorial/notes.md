https://www.youtube.com/watch?v=iWS9ogMPOI0&t=13s

pip install fastapi
pip install uvicorn

start the server
uvicorn main:app --reload

post to the server
curl -X POST -H "Content-Type": application/json" 'http://127/0.0.1:8000/items?item=apple'

get item from server
curl -X GET http://127.0.0.1:8000/items/0