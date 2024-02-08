from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Patient, BloodDonationRecord, Donor

# begin function
def create_patient(
        session: Session,
        name: str,
        surname: str,
        diagnosis: str,
        blood_group: str, 
        rh_factor: str
):
    new_patient = Patient(
        name=name,
        surname=surname,
        diagnosis=diagnosis,
        blood_group=blood_group,
        rh_factor=rh_factor
    )

    session.add(new_patient)

    return new_patient
# end function    


def get_patients(session):
    patients = (
        session.query(Patient)
    ).all()
    
    return patients


def get_patients_with_donor(session: Session):
    patients_with_donor = (
        session.query(BloodDonationRecord, Patient, Donor)
        .join(Patient, BloodDonationRecord.patient_id == Patient.id)
        .join(Donor, BloodDonationRecord.donor_id == Donor.id)
        .all()
    )
    
    return patients_with_donor

# если пациент нет в таблице донорская запись, он стоит в очереди
def get_patients_in_queue(session: Session):
    patients_in_queue = (
        session.query(Patient)
        .outerjoin(BloodDonationRecord, BloodDonationRecord.patient_id == Patient.id)
        .filter(BloodDonationRecord.id == None) 
        .all()
    )
    
    return patients_in_queue



def count_patients_in_queue(session):
    subquery = (
        session.query(func.count())
        .select_from(Patient)
        .outerjoin(BloodDonationRecord, BloodDonationRecord.patient_id == Patient.id)
        .filter(BloodDonationRecord.id == None)
        .scalar_subquery()
    )
    count = session.query(subquery).scalar()
    return count