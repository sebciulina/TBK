# Sebastian Gransicki S22990
Przed uruchomieniem dodać ````127.0.0.1 lab6zad3.com```` po wykonaniu polecenia ````sudo nano /etc/hosts````

Uruchamianie kontenerów:
````
docker build -t z3flask flask/.
docker build -t z3express express/.

docker container run --rm -d --name postgres --label traefik.port=5432 -v "/mnt/c/Users/sebastian/Desktop/Szkola/TBK/6/zad3/database":/docker-entrypoint-initdb.d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=l6z3 postgres:11.5-alpine

docker container run --rm -d --name express --label traefik.enable=true --label traefik.port=3000 --label traefik.priority=1 --label traefik.http.routers.express.rule="Host(\"lab6zad3.com\")" z3express

docker container run --rm -d --name flask --label traefik.enable=true --label traefik.port=9000 --label traefik.priority=10 --label traefik.http.routers.flask.rule="Host(\"lab6zad3.com\") && PathPrefix(\"/cars\")" z3flask

docker run -d --name traefik -p 8080:8080 -p 80:80 -v /var/run/docker.sock:/var/run/docker.sock traefik:latest --api.insecure=true --providers.docker
````
Wywoływanie zapytań:

````lab6zad3.com/cars```` - wyświetlenie wszystkich aut

````lab6zad3.com/cars?year=2011```` - wyświetlenie aut z rokiem 2011

````lab6zad3.com/addCar```` - dodanie nowego samochodu do tablicy w postaci