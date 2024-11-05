import re

class Treatment:
    def __init__(self, treatment_id, patient, doctor, description, date):
        self.treatment_id = treatment_id
        self.patient = patient
        self.doctor = doctor
        self.description = self.validate_description(description)
        self.date = self.validate_date(date)

    def validate_description(self, description):  # Ahora incluye 'self'
        if description == "":
            raise ValueError("La descripción no debe ser vacía")
        return description
    
    def validate_date(self, date):  # Ahora incluye 'self'
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
            raise ValueError("Fecha no válida")
        return date
    
    def record_treatment(self, description, date):
        self.description = self.validate_description(description)
        self.date = self.validate_date(date)
    
    def update_treatment(self, description):
        self.description = self.validate_description(description)
        
    def summary(self):
        return {
            "ID_TRATAMIENTO": self.treatment_id,
            "PACIENTE": self.patient,
            "DOCTOR": self.doctor,
            "DESCRIPCIÓN": self.description,
            "FECHA": self.date
        }
