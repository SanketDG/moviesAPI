# Movies API

This API is hosted on Heroku at https://blooming-thicket-80739.herokuapp.com/movies/

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

_For the following operations, One would also have to be an administrator, I have created a administrator account for the heroku deployment_.

```
Username: admin
Password: fynd1234
```

To create a movie:

```
http -a admin:fynd1234 POST https://blooming-thicket-80739.herokuapp.com/movies/ name=Titanic genre:='["Drama"]' director="James Cameron" imdb_score=8.3 popularity=99
```

To update a movie:

```
http -a admin:fynd1234 PUT https://blooming-thicket-80739.herokuapp.com/movies/<id> name=Titanic genre:='["Drama"]' director="James Cameron" imdb_score=8.5 popularity=99
```

The json body (for Postman and other tools)

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
