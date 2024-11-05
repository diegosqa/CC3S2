import re

class Patient:
    def __init__(self, patient_id, name, dob):
        self.patient_id = patient_id
        self.name = self.validate_name(name)
        self.dob = self.validate_dob(dob)
        self.medical_history = []

    def validate_name(self, name):
        # Permite letras, espacios, puntos y caracteres acentuados
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s.]+$", name):
            raise ValueError("Nombre no válido")
        return name

    def validate_dob(self, dob):
        if not re.match(r"^\d{2}-\d{2}-\d{4}$", dob):
            raise ValueError("Fecha no válida")
        return dob

    def update_info(self, name, dob):
        self.name = self.validate_name(name)
        self.dob = self.validate_dob(dob)

    def add_medical_history(self, entry):
        self.medical_history.append(entry)

    def summary(self):
        return {
            "ID_PACIENTE": self.patient_id,
            "Nombre": self.name,
            "Fecha de nacimiento": self.dob,
            "Historial médico": self.medical_history
        }

