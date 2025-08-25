# percona-study

## Running
```
docker build --platform=linux/amd64 -t custom-mysql .
docker run --platform=linux/amd64 --name mydb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=mySchema custom-mysql:latest
```

## Running mysql
```
mysql -p secret
```

## Running percona toolkit
```
pt-mysql-summary --user=root --password=secret --host=127.0.0.1 --port=3306
```