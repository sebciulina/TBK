# Sebastian Gransicki S22990

````docker build -t z2server server/.```` - Buduje obraz dla serwera z Dockerfile

````docker build -t z2client client/.```` - Buduje obraz dla klienta z Dockerfile

````docker network create z2```` - Tworzymy sieć o nazwie z2

````docker run -d --name server --network z2 -p 9000:9000 z2server```` - Tworzymy kontener z obrazu serwera, dołączamy go do sieci z2 i uruchamiamy go w tle pod portem 9000

````docker run -d --name client --network z2 -p 3000:3000 z2client```` - Tworzymy kontener z obrazu klienta, dołączamy go do sieci z2 i uruchamiamy go w tle pod portem 3000, otrzymujemy odpowiedź od serwera w postaci JSON
