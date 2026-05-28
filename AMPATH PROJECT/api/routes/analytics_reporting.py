from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["Analytics & Reporting"])

@router.get("/operational-dashboard", summary="Operational Dashboards")
def operational_dashboards():
    return {"module": "Analytics & Reporting", "page": "Operational Dashboards"}

@router.get("/incidents", summary="Incident Analytics")
def incident_analytics():
    return {"module": "Analytics & Reporting", "page": "Incident Analytics"}

@router.get("/patients", summary="Patient Analytics")
def patient_analytics():
    return {"module": "Analytics & Reporting", "page": "Patient Analytics"}

@router.get("/financial", summary="Financial Analytics")
def financial_analytics():
    return {"module": "Analytics & Reporting", "page": "Financial Analytics"}

@router.get("/research-kpis", summary="Research KPIs")
def research_kpis():
    return {"module": "Analytics & Reporting", "page": "Research KPIs"}

@router.get("/export", summary="Export Center")
def export_center():
    return {"module": "Analytics & Reporting", "page": "Export Center"}

