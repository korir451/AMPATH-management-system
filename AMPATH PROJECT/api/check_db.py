import os

from api.database import engine


def main() -> None:
    print("DATABASE URL:", engine.url)
    print("HOST env:", os.getenv("DB_HOST"))

    try:
        with engine.connect() as c:
            res = c.execute("SELECT 1")
            print("✅ DB reachable. Result:", list(res))
    except Exception as e:
        print("❌ DB connection failed:", e)


if __name__ == "__main__":
    main()


