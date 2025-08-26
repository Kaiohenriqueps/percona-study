# percona-study

## Running
```
docker-compose up
```

## Running mysql
```
mysql -u <user> -p <password>
```

## Running percona toolkit
1) MySQL Summary example
```
pt-mysql-summary --user=<user> --password=<password> --host=127.0.0.1 --port=3306
```

2) Archiver example
```
pt-archiver --source D=mydb,t=users,u=<user>,p=<password> --dest D=mydb,t=users_tmp,u=<user>,p=changethispassword --where "1=1" --limit 10 --commit-each
```