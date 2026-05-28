from fastapi import APIRouter

router = APIRouter(prefix="/pharmacy-lab", tags=["Pharmacy & Laboratory"])

@router.get("/drug-inventory", summary="Drug Inventory")
def drug_inventory():
    return {"module": "Pharmacy & Laboratory", "page": "Drug Inventory"}

@router.get("/dispensing", summary="Dispensing")
def dispensing():
    return {"module": "Pharmacy & Laboratory", "page": "Dispensing"}

@router.get("/lab-requests", summary="Lab Requests")
def lab_requests():
    return {"module": "Pharmacy & Laboratory", "page": "Lab Requests"}

@router.get("/results", summary="Results")
def results():
    return {"module": "Pharmacy & Laboratory", "page": "Results"}

@router.get("/stock-alerts", summary="Stock Alerts")
def stock_alerts():
    return {"module": "Pharmacy & Laboratory", "page": "Stock Alerts"}

