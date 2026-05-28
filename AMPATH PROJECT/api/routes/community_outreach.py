from fastapi import APIRouter

router = APIRouter(prefix="/outreach", tags=["Community Outreach"])

@router.get("/programs", summary="Outreach Programs")
def outreach_programs():
    return {"module": "Community Outreach", "page": "Outreach Programs"}

@router.get("/mobile-clinics", summary="Mobile Clinics")
def mobile_clinics():
    return {"module": "Community Outreach", "page": "Mobile Clinics"}

@router.get("/volunteers", summary="Volunteers")
def volunteers():
    return {"module": "Community Outreach", "page": "Volunteers"}

@router.get("/vaccination-campaigns", summary="Vaccination Campaigns")
def vaccination_campaigns():
    return {"module": "Community Outreach", "page": "Vaccination Campaigns"}

@router.get("/reports", summary="Reports")
def reports():
    return {"module": "Community Outreach", "page": "Reports"}

