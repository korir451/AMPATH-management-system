from fastapi import APIRouter

router = APIRouter(tags=["Staff Portal"])

@router.get("/staff/dashboard", summary="Staff Dashboard")
def dashboard():
    return {"module": "Staff Portal", "page": "Dashboard"}


@router.get("/attendance", summary="Attendance")
def attendance():
    return {"module": "Staff Portal", "page": "Attendance"}

@router.get("/duty-schedules", summary="Duty Schedules")
def duty_schedules():
    return {"module": "Staff Portal", "page": "Duty Schedules"}

@router.get("/leave-requests", summary="Leave Requests")
def leave_requests():
    return {"module": "Staff Portal", "page": "Leave Requests"}

@router.get("/tasks", summary="Tasks")
def tasks():
    return {"module": "Staff Portal", "page": "Tasks"}

@router.get("/internal-messaging", summary="Internal Messaging")
def internal_messaging():
    return {"module": "Staff Portal", "page": "Internal Messaging"}

@router.get("/department-workspace", summary="Department Workspace")
def department_workspace():
    return {"module": "Staff Portal", "page": "Department Workspace"}

