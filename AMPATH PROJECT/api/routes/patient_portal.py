from fastapi import APIRouter

router = APIRouter(tags=["Patient Portal"])

@router.get("/patients/dashboard", summary="Patient Dashboard")
def dashboard():
    return {"module": "Patient Portal", "page": "Dashboard"}


@router.get("/patients/appointments", summary="Patient Appointments")
def appointments():
    return {"module": "Patient Portal", "page": "Appointments"}


@router.get("/medical-records", summary="Medical Records")
def medical_records():
    return {"module": "Patient Portal", "page": "Medical Records"}

@router.get("/laboratory-results", summary="Laboratory Results")
def laboratory_results():
    return {"module": "Patient Portal", "page": "Laboratory Results"}

@router.get("/prescriptions", summary="Prescriptions")
def prescriptions():
    return {"module": "Patient Portal", "page": "Prescriptions"}

@router.get("/billing-insurance", summary="Billing & Insurance")
def billing_insurance():
    return {"module": "Patient Portal", "page": "Billing & Insurance"}

@router.get("/notifications", summary="Notifications")
def notifications():
    return {"module": "Patient Portal", "page": "Notifications"}

@router.get("/messages", summary="Messaging")
def messages():
    return {"module": "Patient Portal", "page": "Messaging"}

