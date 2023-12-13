## BBC Crawler

A web crawler for [BBC](https://www.bbc.com)

## Tech Stacks

Python and Scrapy.

## Setup

```
cd bbc
docker compose up -d --build
```

## check data from mongoDB

```
docker exec -it bbc_mongo_1 mongosh
```
