CREATE USER backend WITH PASSWORD 'backend';
ALTER ROLE backend SET client_encoding TO 'utf8';
ALTER ROLE backend SET default_transaction_isolation TO 'read committed';
ALTER ROLE backend SET timezone TO 'UTC';
ALTER USER backend CREATEDB;


CREATE DATABASE backend;
GRANT ALL PRIVILEGES ON DATABASE backend TO backend;
