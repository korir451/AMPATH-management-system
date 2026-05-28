from fastapi import APIRouter

router = APIRouter(prefix="/finance", tags=["Finance & Procurement"])

@router.get("/billing", summary="Billing")
def billing():
    return {"module": "Finance & Procurement", "page": "Billing"}

@router.get("/payroll", summary="Payroll")
def payroll():
    return {"module": "Finance & Procurement", "page": "Payroll"}

@router.get("/procurement", summary="Procurement")
def procurement():
    return {"module": "Finance & Procurement", "page": "Procurement"}

@router.get("/inventory", summary="Inventory")
def inventory():
    return {"module": "Finance & Procurement", "page": "Inventory"}

@router.get("/vendors", summary="Vendor Management")
def vendors():
    return {"module": "Finance & Procurement", "page": "Vendor Management"}

@router.get("/financial-reports", summary="Financial Reports")
def financial_reports():
    return {"module": "Finance & Procurement", "page": "Financial Reports"}

