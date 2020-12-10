# Movies API

This API is hosted on Heroku at

Test the API:

_For the following operations, one would need an API testing tool something like `Postman`, or [`httpie.io`](https://httpie.io)_

Get All Movies

```
http GET https://blooming-thicket-80739.herokuapp.com/movies/
```

Get a single movie by ID

```
http GET https://blooming-thicket-80739.herokuapp.com/movies/<id>
```

---

_For the following operations, One would also have to be an administrator, I have created a administrator account_

```
Username: admin
Password: fynd1234
```

To create/update a movie:

```
http -a admin:fynd1234 POST https://blooming-thicket-80739.herokuapp.com/movies/ name=Titanic genre:='["Drama"]' director="James Cameron" imdb_score=8.3 popularity=99
```

Note: Replace `POST` with `PUT` or `PATCH` to replace objects

The json body

```json
{
    name: "Titanic",
    genre: ["Drama"]
    director: "James Cameron"
    imdb_score: 8.3
    popularity: 99
}
```

To delete a Movie

```
http -a admin:fynd1234 DELETE https://blooming-thicket-80739.herokuapp.com/movies/<id>
```

To update a Movie
