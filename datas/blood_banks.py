from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import BloodBank

# begin function
def create_bloodBank(
        session: Session,
        name: str,
        address: str,
        contact_info: str
):
    new_bloodBank = BloodBank(
        name=name,
        address=address,
        contact_info=contact_info
    )

    session.add(new_bloodBank)

    return new_bloodBank
# end function    



def get_blood_banks(session):
    banks = (
        session.query(BloodBank)
    ).all()
    
    return banks