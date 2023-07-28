from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Vulnerability(db.Model):
    __tablename__ = "vulnerability"
    id = db.Column(db.Integer, primary_key=True)
    cve = db.Column(db.String(20), nullable=False)
    cvss = db.Column(db.Float, nullable=False, default=99.0)
    vuln_name = db.Column(db.String(100), nullable=False)
    exploit_available = db.Column(
        db.String(10), nullable=False, default="Unknown")
    created_date = db.Column(db.DateTime(), nullable=False)
    updated_date = db.Column(db.DateTime(), nullable=True)
    check_date = db.Column(db.DateTime(), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Vulnerability {self.cve}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'cve': self.cve,
            'cvss': self.cvss,
            'vuln_name': self.vuln_name,
            'exploit_available': self.exploit_available,
            'created_date': self.created_date,
            'updated_date': self.updated_date,
            'check_date': self.check_date,
            'notes': self.notes
        }
