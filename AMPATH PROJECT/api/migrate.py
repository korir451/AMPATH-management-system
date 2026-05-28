"""Create database tables directly from SQLAlchemy models.

This is a simple starter approach (no Alembic migrations yet).
Run once after starting Postgres.

Usage:
  python -m api.migrate
"""

from api.database import engine
from api.models import (  # noqa: F401
    Application,
    Appointment,
    Incident,
    News,
    Patient,
    Research,
    User,
)
from api.database import Base


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created (if not already present).")


if __name__ == "__main__":
    main()

