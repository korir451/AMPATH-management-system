# AMPATH MySQL Database Provisioning (Demo)

This project uses SQLAlchemy with a MySQL engine defined in `api/database.py`:

- Database: `ampath_db`
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: `Brian3943*`

## 1) Create the database
Run this in MySQL (or phpMyAdmin SQL tab):

```sql
CREATE DATABASE IF NOT EXISTS ampath_db;
```

## 2) Verify connectivity
In MySQL, you can verify tables after migrations run.

## 3) Run migrations
Migrations depend on your existing migration tooling in this repo (`api/migrate.py`).

If your migrations fail because the DB does not exist, ensure step (1) ran successfully.

## Notes
- If your MySQL user/password differs from `root:Brian3943*`, update `api/database.py`.
- This is demo/presentation mode; not production hardened.

