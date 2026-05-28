from fastapi import APIRouter

router = APIRouter(prefix="/incidents", tags=["Incident Reporting"])

@router.post("/report", summary="Report Incident")
def report_incident():
    return {"module": "Incident Reporting", "action": "report_incident"}

@router.get("/inbox", summary="Incident Inbox")
def inbox():
    return {"module": "Incident Reporting", "page": "Incident Inbox"}

@router.get("/investigation", summary="Investigation Workflow")
def investigation_workflow():
    return {"module": "Incident Reporting", "page": "Investigation Workflow"}

@router.post("/evidence", summary="Evidence Management")
def evidence_management():
    return {"module": "Incident Reporting", "action": "evidence_management"}

@router.get("/sla", summary="SLA Tracking")
def sla_tracking():
    return {"module": "Incident Reporting", "page": "SLA Tracking"}

@router.get("/escalations", summary="Escalation Rules")
def escalation_rules():
    return {"module": "Incident Reporting", "page": "Escalation Rules"}

@router.get("/analytics", summary="Incident Analytics")
def incident_analytics():
    return {"module": "Incident Reporting", "page": "Incident Analytics"}

