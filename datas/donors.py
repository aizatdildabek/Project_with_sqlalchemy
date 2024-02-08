from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Donor

# begin function
def create_donor(
        session: Session,
        name: str,
        surname: str,
        blood_group: str,
        rh_factor: str
):
    new_donor = Donor(
        name=name,
        surname=surname,
        blood_group=blood_group,
        rh_factor=rh_factor
    )

    session.add(new_donor)

    return new_donor
# end function    

def get_donors(session):
    donors = (
        session.query(Donor)
    ).all()
    
    return donors
