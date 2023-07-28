from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app.models import Vulnerability, db

bp = Blueprint("vuln", __name__, template_folder="../templates")


@bp.route("/vuln")
def VulnList():
    vulns = [
        {
            "id": 1,
            "cve": "CVE-2023-1234",
            "cvss": 7.5,
            "vuln_name": "Remote Code Execution",
            "exploit_available": "Yes",
            "created_date": "2023-07-10",
            "updated_date": "2023-07-15",
            "check_date": "2023-07-20",
            "notes": "This is a note"
        },
        {
            "id": 2,
            "cve": "CVE-2023-9876",
            "cvss": 6.8,
            "vuln_name": "Denial of Service",
            "exploit_available": "No",
            "created_date": "2023-07-01",
            "updated_date": "2023-07-10",
            "check_date": "2023-07-20",
            "notes": "This is a note"
        },
        {
            "id": 3,
            "cve": "CVE-2023-5432",
            "cvss": 9.1,
            "vuln_name": "Remote Privilege Escalation",
            "exploit_available": "Yes",
            "created_date": "2023-07-03",
            "updated_date": "2023-07-18",
            "check_date": "2023-07-20",
            "notes": "This is a note"
        }

    ]

    return render_template("vulnerability/list.html", vulns=vulns)


@bp.route("/vuln/add", methods=["POST"])
def VulnAdd():
    cve = request.form["cve"]
    cvss = request.form["cvss"]
    vuln_name = request.form["vuln_name"]
    exploit_available = request.form["exploit_available"]
    now = datetime.now()
    created_date = now.strptime('%d/%m/%Y %H:%M:%S')
    notes = request.form["notes"]

    vuln = Vulnerability(cve=cve, cvss=cvss, vuln_name=vuln_name,
                         exploit_available=exploit_available, created_date=created_date, notes=notes)
    db.session.add(vuln)
    db.session.commit()

    return redirect(url_for("vuln.VulnList"))
