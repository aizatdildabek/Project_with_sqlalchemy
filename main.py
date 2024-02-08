from datas.donors import create_donor, get_donors
from datas.patients import create_patient, get_patients, count_patients_in_queue, get_patients_in_queue, get_patients_with_donor
from datas.blood_banks import create_bloodBank, get_blood_banks
from datas.danation_records import create_donation_records, get_records
from database import get_session
import datetime

if __name__ == '__main__':

    session = get_session()

    new_donor = create_donor(
        session=session,
        name="Darmen",
        surname="Darmenov",
        blood_group="AB+",
        rh_factor="+"
    )
    print("Added new donor factor:", new_donor.rh_factor)

    new_patient = create_patient(
        session=session,
        name="Айжулдыз",
        surname="Кадыров",
        diagnosis="Анемия",
        blood_group="AО+",
        rh_factor="+"
    )
    print("Поступил запрос на следующую группу крови:", new_patient.blood_group)


    new_bloodbank = create_bloodBank(
        session=session,
        name="Городская",
        address="Момышулы 37",
        contact_info="Тел: +77774445566"
    )

    new_donation_record = create_donation_records(
        session=session, 
        donor_id=3,
        patient_id=2,
        bank_id=2,
        donation_date=datetime.datetime(2024, 2, 1)
    )

    patients = get_patients(session)

    for patient in patients:
        print(f"Имя: {patient.name} - {patient.blood_group}({patient.diagnosis})")


    donors = get_donors(session)

    for donor in donors:
        print(f"Имя: {donor.name}, группа крови:{donor.blood_group}(резус фактор:{patient.rh_factor})")
       
    # Так же можем выводит(увидеть) список банки крови и список донорскую запись. (get_blood_banks, get_records)   

    # Пациент могут узнать кто ему давал крови.
    patients_with_donor = get_patients_with_donor(session)
    for record, patient, donor in patients_with_donor:
        print(f"Донорский список ID: {record.id}, Имя пациента: {donor.name}, Имя донора: {patient.name}")
        

    patients_in_queue = get_patients_in_queue(session)
    for patient in patients_in_queue:
        print("Идентификатор пациента в очереди:", patient.id)

    count = count_patients_in_queue(session)
    print("Количество пациентов в очереди:", count)


    session.commit()
    session.close()