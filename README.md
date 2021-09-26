# Exercitiul cu Docker

## Input

- porneste un server de http pe portul 8080 in container `si nu expune niciun port in exteriorul lui`
``` 
docker run -it --rm --name my-test-1 python:latest python -m http.server 8080
```

- executa o comanda in interiorul containerului
```
docker exec my-test-1 wget http://localhost:8080
```

## Output

1. Explain what “localhost” refers to from http://localhost:8080 
- Serverul este rulat pe `localhost-ul` din interiorul containerului si nu se expune niciun port in exteriorul lui


2. Try http://localhost:8080. in the browser. How do you make it work?
- Trebuie sa adaugam o mapare a portului din container cu un port de pe host(masina noastra)
```
docker run -it -p 8080:8080 --rm --name my-test-1 python:latest python -m http.server 8080
```

3. Make it at the following url http://localhost:10080 in the browser
- Portul 10080 este un port unsafe. Pentru a putea sa rulam serverul pe acest port, trebuie sa facem cateva configuratii in browser. Este mai usor sa rulam pe un alt port:
```
docker run -it -p 10081:8080 --rm --name my-test-1 python:latest python -m http.server 8080
```

4. Make it print the contents of a folder from your local machine (any folder)
- pentru a realiza aceasta cerinta, trebuie sa montam un folder de pe masina locala in container, folosind argumentul mount:
```
docker run -it -p 10081:8080 --mount 'type=bind,source=/home/adrian/Documents/algo,target=/app' --rm --name my-test-1 python:latest python -m http.server 8080
```
