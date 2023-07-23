from flask import Blueprint, render_template

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


@bp.route("/vuln/add")
def VulnAdd():
    return render_template("vulnerability/add.html")
