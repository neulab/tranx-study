# Task Description

You are expected to write an HTTP server that listens to `127.0.0.1 (localhost)` on port `8000`.

The server should be started by running `python main.py`.

The server exposes an HTTP GET API endpoint at `http://localhost:8000/query`, where the user should supply two query parameters: `email` and `ip`.
The API will query the person data listed in the file `data.csv`, and find the entry with both the queried email address and IP address, and respond with the first name, last name and gender in the following JSON format:
```
{
    "first_name": "Merry",
    "last_name": "MacKettrick",
    "gender": "Male"
}
```

Note that, if the provided value to parameter `email` is not in valid format (someone@somewhere.xxx) or  `ip` provided is not in valid format as defined by IP address, the response should be empty with HTTP code `400 Bad Request`.
If no matching record is found in the data file given provided query parameters, the response should be empty with HTTP code `404 Not Found`.


# Recommended Libraries (Installed)
```
requests
flask
django
```

# Example Output

```
$ python main.py
(running, open another terminal session)
$ curl -G -v "http://localhost:8000/query" --data-urlencode "email=mmackettrick0@latimes.com" --data-urlencode "ip=233.43.85.181"
*   Trying localhost...
* TCP_NODELAY set
* Connected to localhost port 8000 (#0)
> GET /?email=mmackettrick0%40latimes.com&ip=233.43.85.181 HTTP/1.1
> Host: localhost
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 200 OK
...
...
...

{
    "first_name": "Merry",
    "last_name": "MacKettrick",
    "gender": "Male"
}


$ curl -G -v "http://localhost:8000/query" --data-urlencode "email=badformat.com" --data-urlencode "ip=12345.bad.format"
*   Trying localhost...
* TCP_NODELAY set
* Connected to localhost port 8000 (#0)
> GET /?email=mmackettrick0%40latimes.com&ip=233.43.85.181 HTTP/1.1
> Host: localhost
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 400 Bad Request
<
(should be empty)

$ curl -G -v "http://localhost:8000/query" --data-urlencode "email=notexist@company.com" --data-urlencode "ip=1.1.1.1"
*   Trying localhost...
* TCP_NODELAY set
* Connected to localhost port 8000 (#0)
> GET /?email=mmackettrick0%40latimes.com&ip=233.43.85.181 HTTP/1.1
> Host: localhost
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 404 Not Found
<
(should be empty)

```