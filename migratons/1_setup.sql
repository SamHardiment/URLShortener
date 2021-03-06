DROP TABLE IF EXISTS urllist;

CREATE TABLE urllist (
  id serial PRIMARY KEY,
  long_url varchar(255) NOT NULL,
  short_url varchar(50) NOT NULL
);

DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
  id serial PRIMARY KEY,
  long_url varchar(255) NOT NULL,
  short_url varchar(50) NOT NULL
);
