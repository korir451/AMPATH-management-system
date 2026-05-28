# TODO - AMPATH Management System

## Backend & Frontend Department Structure (Routes + Pages)

### Research Portal upgrade (Phase 2)

- [x] Step R0: Reviewed current backend `/research/*` endpoints (placeholders)
- [x] Step R1: Confirmed existing frontend `frontend/research-proposal.html` and home link in `frontend/index.html`
- [x] Step R2: Create Research Portal navigation scaffolding for new research modules (sidebar/topbar pattern)
- [x] Step R3: Upgrade `frontend/research-proposal.html` to a proposal management page compatible with the new workflow
- [x] Step R4: Create `frontend/research-dashboard.html` (Research Command Center)
- [x] Step R5: Create `frontend/proposal-review.html` (proposal review)
- [x] Step R6: Create `frontend/ethics-dashboard.html` (ethics committee dashboard)
- [x] Step R7: Create `frontend/ethics-review.html` (ethics review workflow)
- [ ] Step R8: Create `frontend/clinical-trials.html`
- [ ] Step R9: Create `frontend/publications.html`
- [ ] Step R10: Create `frontend/research-documents.html`
- [ ] Step R11: Create `frontend/research-analytics.html`
- [ ] Step R12: Create `frontend/research-reports.html`
- [ ] Step R13: Create `frontend/grants-management.html`
- [ ] Step R14: Update `frontend/index.html` Research tile to point to `frontend/research-dashboard.html`
- [ ] Step R15: (Optional next) Add lightweight JS stubs on research pages to call placeholder FastAPI endpoints


### MVP / Incident & Staff Portal (Phase 1)
- [ ] Step 1: Shared layout foundation (sidebar/topbar/footer) + responsive CSS
- [ ] Step 2: STAFF DASHBOARD upgrade (replace `frontend/staff_portal.html`)
- [ ] Step 3: Create missing staff-only pages for all modules (patients, appointments, attendance/shifts, tasks, departments, internal comms, research, training, inventory/pharmacy, analytics, emergency ops, profile/settings, security)
- [ ] Step 4: INCIDENT REPORTING separation verification (ensure staff dashboard links to `frontend/staff_incidents.html`)
- [ ] Step 5: Cross-linking checks across navigation
- [ ] Step 6: Backend preparation (wire UI placeholders)
- [ ] Step 7: Tests/smoke + final run instructions

