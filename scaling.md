# Scaling Movies Service

## Database

### Indexing

Since there are lots of users, there will be lots of movies
created. Hence the GET and SEARCH results will involve fetching a lot of data.
This can be sped up by using indexes on the rows that will be used the most
during retrieving, searching.

### Replication

The database itself can have a single leader database solely for writes, and N
followers for reading data. Since writes to the database are solely reserved to admins, a single leader database would be enough. Reads will be done by millions
of users, so it's important to have atleast enough followers, so that if one goes down, any other follower can be used. We acheive availability. To achieve consistency, meaning that we want the data replication from leaders to followers to be as fast as possible, we have the CAP theorem hurdle, where we can't achieve both consistency and availability if we assume that parition tolerance is inveitable for
any system. So in conclusion, we will achieve eventual consistency, where some of our users will inevitably see the old data due to delay in data propogation.

## Caching

Caching in this case means caching on the server.

The most naive way to go about this is to use a in-memory store for storing the least recently used (read accessed) movies in the store. When the API user wants to access
a movie's details, the in-memory store is first searched by the movie's ID and if it's a miss, then the database is searched. This can be also useful in search operations.

A better algorithm to use here would be to calculate the frequency count of each movie accessed and design a cache eviction policy which rewards the top N most frequently accessed movies and evicts anything lower than that.

## Misc. speedups

### Move to asyncio!

Even though there are multiple processes/threads configured at the server level which is why the interpreter will not block on I/O operations, asyncio can be really helpful to achieve co-operative multitasking inside a single process or a single thread. Moving to ASGI can also increase the server throughput.

### Use the right set of middleware

### Implement pagination at the database level
