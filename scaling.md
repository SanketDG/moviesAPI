# Scaling Movies Service

- [Vertical Scaling](#vertical-scaling)
- [Horizontal Scaling / Load Balancing](#horizontal-scaling--load-balancing)
- [Database](#database)
  - [Indexing](#indexing)
  - [Replication](#replication)
  - [SQL Tuning](#sql-tuning)
- [Caching](#caching)
- [Misc. Speedups](#misc-speedups)

## Vertical Scaling

Considering that we may have an in-memory cache (mentioned below) and we will load a lot of
movie data in memory, one would suggest having at least a good amount of RAM on the servers.

## Horizontal Scaling / Load Balancing

Having multiple servers would obviously help here, since we have a large number of hits,
with some form of load balancing based on the least connection algorithm. Periodic health
checks to these servers can also enhance service discovery and uptime.

My personal suggestion is to use something like nginx/HAProxy over the application layer.

## Database

### Indexing

Since there are lots of users, there will be lots of movies
created. Hence, the GET and SEARCH results will involve fetching a lot of data.
This can be sped up by using indexes on the rows that will be used the most
during retrieving, searching.

### Replication

The database itself can have a single leader database solely for writes, and N
followers for reading data. Since writes to the database are solely reserved to admins, a single leader database would be enough. Reads will be done by millions
of users, so it's important to have atleast enough followers, so that if one goes down, any other follower can be used. We achieve availability. To achieve consistency, meaning that we want the data replication from leaders to followers to be as fast as possible, we have the CAP theorem hurdle, where we can't achieve both consistency and availability if we assume that partition tolerance is inevitable for
any system. So in conclusion, we will achieve eventual consistency, where some of our users will inevitably see the old data due to delay in data propagation.

### SQL Tuning

Since a lot of our database logic is abstracted away because of Django's ORM, it might
be worthwhile to spend a significant amount of time to inspect the actual SQL queries
that are being sent to the database, benchmark them and optimize as necessary.

## Caching

Caching in this case means caching on the server.

The most naive way to go about this is to use an in-memory cache for storing the least recently used (read accessed) movies in the cache. When the API user wants to access
a movie's details, the in-memory cache is first searched by the movie's ID and if it's a miss, then the database is searched. This can be also useful in search operations.

A better algorithm to use here would be to calculate the frequency count of each movie accessed and design a cache eviction policy which rewards the top N most frequently accessed movies and evicts anything lower than that.

My personal suggestion would be to use somethig like Redis/memcached as an in-memory cache.

## Misc. Speedups

These speedups are bottlenecks that are only present because of the tech stack used to
develop the application. Hence these are only to be implemented after careful inspection
and benchmarking.

- Move to asyncio!

  - Even though there are multiple processes/threads configured at the server level which is why the interpreter will not block on I/O operations, asyncio can be really helpful to achieve co-operative multitasking inside a single process or a single thread. Moving to ASGI can also increase the server throughput.

- WSGI/ASGI
  - Using the right WSGI/ASGI server is crucial here when we have such high loads.
- Implement pagination at the database level.
  - Pagination is already implemented inside the web API, but the whole dataset is loaded into memory each time, the pagination only exists to serve the API user's needs.
  - Implementing and enforcing pagination at the database level would help with lesser load and lesser memory usage.
