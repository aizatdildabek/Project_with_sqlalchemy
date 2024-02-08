from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, CheckConstraint
from sqlalchemy.orm import relationship

from database import Base, engine


# UNIQUE, NOT NULL
class Donor(Base):
    __tablename__ = 'donors'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    surname = Column(String(30))
    blood_group = Column(String(5))
    rh_factor = Column(String(5))

    blood_donation_records = relationship('BloodDonationRecord', back_populates='donor')


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    surname = Column(String(30))
    diagnosis = Column(String(30))
    blood_group = Column(String(5))
    rh_factor = Column(String(5))

    blood_donation_records = relationship('BloodDonationRecord',uselist=False, cascade='all,delete', back_populates='patient')


class BloodDonationRecord(Base):
    __tablename__ = 'blood_donation_records'

    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey('donors.id', ondelete='CASCADE'), nullable=False, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id', ondelete='CASCADE'), nullable=False, index=True)
    bank_id = Column(Integer, ForeignKey('blood_banks.id', ondelete='CASCADE'), nullable=False, index=True)
    donation_date = Column(Date)

    donor = relationship("Donor", uselist=False, cascade='all,delete', back_populates="blood_donation_records")
    patient = relationship("Patient", uselist=False, cascade='all,delete', back_populates="blood_donation_records")
    bank = relationship("BloodBank", uselist=False, cascade='all,delete', back_populates="blood_donation_records")


class BloodBank(Base):
    __tablename__ = 'blood_banks'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    address = Column(String(30))
    contact_info = Column(String(20))

    blood_donation_records = relationship('BloodDonationRecord', uselist=False, cascade='all,delete', back_populates='bank')

    
# Создаем таблицы в базе данных
Base.metadata.create_all(engine)
