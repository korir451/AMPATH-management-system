from fastapi import FastAPI

from api.routes import analytics_reporting, auth, community_outreach, finance_procurement, incident_reporting, internship_portal, patient_portal, pharmacy_laboratory, public_website, research_portal, staff_portal, super_admin, training_e_learning

app = FastAPI(title="AMPATH API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}

# Public Website
app.include_router(public_website.router)

# Authentication System
app.include_router(auth.router)

# Patient Portal
app.include_router(patient_portal.router)


# Staff Portal
app.include_router(staff_portal.router, prefix="")


# Incident Reporting
app.include_router(incident_reporting.router)

# Internship & Attachment Portal
app.include_router(internship_portal.router)

# Research Portal
app.include_router(research_portal.router)

# Finance & Procurement
app.include_router(finance_procurement.router)

# Pharmacy & Laboratory
app.include_router(pharmacy_laboratory.router)

# Community Outreach
app.include_router(community_outreach.router)

# Training & E-Learning
app.include_router(training_e_learning.router)

# Analytics & Reporting
app.include_router(analytics_reporting.router)

# Super Admin Console
app.include_router(super_admin.router)


