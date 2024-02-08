from sqlalchemy import select, func
from sqlalchemy.orm import Session
from datetime import datetime

from models import BloodDonationRecord

# begin function
def create_donation_records(
        session: Session,
        donor_id: int,
        patient_id:int,
        bank_id: int,
        donation_date: str

):
    new_donation_record = BloodDonationRecord(
        donor_id=donor_id,
        patient_id=patient_id,
        bank_id=bank_id,
        donation_date=donation_date
    )

    session.add(new_donation_record)

    return new_donation_record
# end function    



def get_records(session):
    records = (
        session.query(BloodDonationRecord)
    ).all()
    
    return records
