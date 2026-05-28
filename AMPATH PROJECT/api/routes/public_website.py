from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["Public Website"])

@router.get("/", summary="Public Home")
def home():
    return {"module": "Public Website", "page": "Home"}

@router.get("/about", summary="About")
def about():
    return {"module": "Public Website", "page": "About"}

@router.get("/services", summary="Services")
def services():
    return {"module": "Public Website", "page": "Services"}

@router.get("/departments", summary="Departments")
def departments():
    return {"module": "Public Website", "page": "Departments"}

@router.get("/research", summary="Research")
def research():
    return {"module": "Public Website", "page": "Research"}

@router.get("/news", summary="News & Events")
def news_events():
    return {"module": "Public Website", "page": "News & Events"}

@router.get("/careers", summary="Careers")
def careers():
    return {"module": "Public Website", "page": "Careers"}

@router.get("/contact", summary="Contact")
def contact():
    return {"module": "Public Website", "page": "Contact"}

@router.get("/emergency-hotline", summary="Emergency Hotline")
def emergency_hotline():
    return {"module": "Public Website", "page": "Emergency Hotline"}

