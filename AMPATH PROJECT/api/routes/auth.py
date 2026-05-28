from fastapi import APIRouter

router = APIRouter(tags=["Authentication"])

@router.post("/auth/login", summary="Login")
def login():
    return {"module": "Authentication", "action": "login"}


@router.post("/register", summary="Register")
def register():
    return {"module": "Authentication", "action": "register"}

@router.post("/password-recovery", summary="Password Recovery")
def password_recovery():
    return {"module": "Authentication", "action": "password_recovery"}

@router.post("/mfa-otp", summary="MFA / OTP")
def mfa_otp():
    return {"module": "Authentication", "action": "mfa_otp"}

@router.post("/session/logout", summary="Session Management")
def logout():
    return {"module": "Authentication", "action": "logout"}

