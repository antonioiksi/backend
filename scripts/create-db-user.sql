CREATE USER florizel_backend WITH PASSWORD 'florizel_backend';
ALTER ROLE florizel_backend SET client_encoding TO 'utf8';
ALTER ROLE florizel_backend SET default_transaction_isolation TO 'read committed';
ALTER ROLE florizel_backend SET timezone TO 'UTC';
ALTER USER florizel_backend CREATEDB;


CREATE DATABASE florizel_backend;
GRANT ALL PRIVILEGES ON DATABASE florizel_backend TO florizel_backend;
