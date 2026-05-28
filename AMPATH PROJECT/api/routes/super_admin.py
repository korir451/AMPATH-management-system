from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Super Admin Console"])

@router.get("/users", summary="User Management")
def user_management():
    return {"module": "Super Admin Console", "page": "User Management"}

@router.get("/roles", summary="Role Management")
def role_management():
    return {"module": "Super Admin Console", "page": "Role Management"}

@router.get("/audit-logs", summary="Audit Logs")
def audit_logs():
    return {"module": "Super Admin Console", "page": "Audit Logs"}

@router.get("/system-configuration", summary="System Configuration")
def system_configuration():
    return {"module": "Super Admin Console", "page": "System Configuration"}

@router.get("/api-management", summary="API Management")
def api_management():
    return {"module": "Super Admin Console", "page": "API Management"}

@router.get("/security-controls", summary="Security Controls")
def security_controls():
    return {"module": "Super Admin Console", "page": "Security Controls"}

