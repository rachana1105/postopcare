from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Patient(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    frequency = db.Column(db.String)
    patient_id = db.Column(db.String, db.ForeignKey('patient.id'))

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String)
    date = db.Column(db.String)
    remarks = db.Column(db.String)

class Meditation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String)
    number = db.Column(db.String)
    name = db.Column(db.String)

class Medication(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    end_date = db.Column(db.String)

class Monitoring(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recovery_status = db.Column(db.String)
    doctor_name = db.Column(db.String)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form = request.form
    # TODO: build Patient, Appointment, Consultation, Meditation, Medication,
    # and Monitoring objects from the submitted form fields, then persist them.

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # TODO: query all records for each model and pass them to the template
    return render_template('dashboard.html',
        patients=[],
        appointments=[],
        consultations=[],
        meditations=[],
        medications=[],
        doctor_monitorings=[]
    )

# ─── Delete Routes ───────────────────────────

@app.route("/delete_patient/<string:patient_id>", methods=["POST"])
def delete_patient(patient_id):
    # TODO: look up the Patient record and delete it if found
    return redirect(url_for('dashboard'))

@app.route("/delete_appointment/<int:appointment_id>", methods=["POST"])
def delete_appointment(appointment_id):
    # TODO: look up the Appointment record and delete it if found
    return redirect(url_for('dashboard'))

@app.route("/delete_consultation/<int:consultation_id>", methods=["POST"])
def delete_consultation(consultation_id):
    # TODO: look up the Consultation record and delete it if found
    return redirect(url_for('dashboard'))

@app.route("/delete_meditation/<int:meditation_id>", methods=["POST"])
def delete_meditation(meditation_id):
    # TODO: look up the Meditation record and delete it if found
    return redirect(url_for('dashboard'))

@app.route("/delete_medication/<string:medication_id>", methods=["POST"])
def delete_medication(medication_id):
    # TODO: look up the Medication record and delete it if found
    return redirect(url_for('dashboard'))

@app.route("/delete_doctor_monitoring/<int:monitoring_id>", methods=["POST"])
def delete_doctor_monitoring(monitoring_id):
    # TODO: look up the Monitoring record and delete it if found
    return redirect(url_for('dashboard'))

# ─── Main ─────────────────────────────────────
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
