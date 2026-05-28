from __future__ import annotations

import enum

from sqlalchemy import Date, Enum as SAEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class UserRole(str, enum.Enum):
    patient = "patient"
    staff = "staff"
    admin = "admin"
    researcher = "researcher"
    attachee = "attachee"


class AppointmentStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"


class IncidentSeverity(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    role: Mapped[UserRole] = mapped_column(SAEnum(UserRole), nullable=False)
    created_at: Mapped[str] = mapped_column(String, nullable=True)


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    dob: Mapped[str] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String(10), nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    date: Mapped[str] = mapped_column(Date, nullable=True)
    status: Mapped[AppointmentStatus] = mapped_column(SAEnum(AppointmentStatus), nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    reporter_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    type: Mapped[str] = mapped_column(String(100), nullable=True)
    severity: Mapped[IncidentSeverity] = mapped_column(SAEnum(IncidentSeverity), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="open")
    file: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[str] = mapped_column(String, nullable=True)


class Research(Base):
    __tablename__ = "research"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    category: Mapped[str] = mapped_column(String(100), nullable=True)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    file: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")
    created_at: Mapped[str] = mapped_column(String, nullable=True)


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    position: Mapped[str] = mapped_column(String(100), nullable=True)
    cv: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")


class News(Base):
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[str] = mapped_column(String, nullable=True)

