import pytest
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from treatment import Treatment
from hospital_management import HospitalManagement

# Fixtures para datos de prueba
@pytest.fixture
def sample_patient():
    return Patient(patient_id="001", name="Juan Silva", dob="16-02-2000")

@pytest.fixture
def sample_doctor():
    return Doctor(doctor_id="D001", name="Dra. María Ravichagua", specialization="Cardiología", available_slots=["17-02-2024, 09:00"])

@pytest.fixture
def sample_appointment(sample_patient, sample_doctor):
    return Appointment(appointment_id="A001", patient=sample_patient, doctor=sample_doctor, datetime="17-02-2024, 09:00")

@pytest.fixture
def sample_treatment(sample_patient, sample_doctor):
    return Treatment(treatment_id="T001", patient=sample_patient, doctor=sample_doctor, description="Tratamiento de gripe", date="18-02-2024")

@pytest.fixture
def hospital_management():
    return HospitalManagement()

# Pruebas para la clase Patient
def test_update_info(sample_patient):
    sample_patient.update_info("Carlos Silva", "20-05-1990")
    assert sample_patient.name == "Carlos Silva"
    assert sample_patient.dob == "20-05-1990"

def test_update_info_invalid_name(sample_patient):
    with pytest.raises(ValueError, match="Nombre no válido"):
        sample_patient.update_info("", "20-05-1990")

def test_add_medical_history(sample_patient):
    sample_patient.add_medical_history("Diagnóstico de gripe")
    assert "Diagnóstico de gripe" in sample_patient.medical_history

# Pruebas para la clase Doctor
def test_add_available_slot(sample_doctor):
    sample_doctor.add_available_slot("18-02-2024, 10:00")
    assert "18-02-2024, 10:00" in sample_doctor.available_slots

def test_remove_available_slot(sample_doctor):
    sample_doctor.remove_available_slot("17-02-2024, 09:00")
    assert "17-02-2024, 09:00" not in sample_doctor.available_slots

def test_remove_nonexistent_slot(sample_doctor, capsys):
    sample_doctor.remove_available_slot("19-02-2024, 11:00")
    captured = capsys.readouterr()
    assert "El slot no existe. No hay nada que eliminar" in captured.out

# Pruebas para la clase Appointment
def test_schedule(sample_appointment):
    sample_appointment.schedule()
    assert sample_appointment.status == "scheduled"
    assert "17-02-2024, 09:00" not in sample_appointment.doctor.available_slots

def test_schedule_unavailable_slot(sample_appointment):
    sample_appointment.doctor.available_slots.remove("17-02-2024, 09:00")
    with pytest.raises(ValueError, match="La cita no está disponible"):
        sample_appointment.schedule()

def test_cancel(sample_appointment):
    sample_appointment.schedule()
    sample_appointment.cancel()
    assert sample_appointment.status == "cancelled"
    assert "17-02-2024, 09:00" in sample_appointment.doctor.available_slots

# Pruebas para la clase Treatment
def test_record_treatment(sample_treatment):
    sample_treatment.record_treatment("Nuevo tratamiento de fiebre", "19-02-2024")
    assert sample_treatment.description == "Nuevo tratamiento de fiebre"
    assert sample_treatment.date == "19-02-2024"

def test_update_treatment(sample_treatment):
    sample_treatment.update_treatment("Actualización del tratamiento de gripe")
    assert sample_treatment.description == "Actualización del tratamiento de gripe"

# Pruebas para la clase HospitalManagement
def test_manage_patients_create(hospital_management):
    hospital_management.manage_patients("create", "001", "Ana Gómez", "12-03-1992")
    assert "001" in hospital_management.patients

def test_manage_patients_update(hospital_management):
    hospital_management.manage_patients("create", "001", "Diego Quispe", "12-03-1992")
    hospital_management.manage_patients("update", "001", "Diego Q.", "15-05-1992")
    assert hospital_management.patients["001"].name == "Diego Q."

def test_manage_patients_delete(hospital_management):
    hospital_management.manage_patients("create", "001", "Ana Gómez", "12-03-1992")
    hospital_management.manage_patients("delete", "001", None, None)
    assert "001" not in hospital_management.patients

# Pruebas de cobertura de caminos y MC/DC
def test_schedule_and_cancel_full_path(sample_appointment):
    sample_appointment.schedule()
    sample_appointment.cancel()
    assert sample_appointment.status == "cancelled"
    assert "17-02-2024, 09:00" in sample_appointment.doctor.available_slots

