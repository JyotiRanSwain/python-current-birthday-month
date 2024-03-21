# This setup creates a simple Flask web application. When you run app.py, you can access the HTML page at http://127.0.0.1:5000/


Build docker image:
```
docker build -t flask-app .
```

Create docker container:
```
docker run -d --name Birthday -p 5000:5000 -v .\employees.xlsx:/app/employees.xlsx flask-app
```
