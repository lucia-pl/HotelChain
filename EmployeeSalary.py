import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class EmployeeSalary:
    """
    Clase que utiliza lógica difusa para calcular el multiplicador salarial 
    basado en el puesto de trabajo y la calificación del hotel.
    """
    
    def __init__(self):
        """
        Inicializa las variables difusas y define las reglas de decisión.
        """
        self.job_position = ctrl.Antecedent(np.arange(1, 6, 1), 'job_position')
        self.hotel_rating = ctrl.Antecedent(np.arange(3, 6, 1), 'hotel_rating')

        self.salary_multiplier = ctrl.Consequent(np.arange(0.8, 2.1, 0.1), 'salary_multiplier')

        self.job_position['junior'] = fuzz.trimf(self.job_position.universe, [1, 1, 2])
        self.job_position['mid'] = fuzz.trimf(self.job_position.universe, [2, 3, 4])
        self.job_position['senior'] = fuzz.trimf(self.job_position.universe, [3, 4, 5])
        self.job_position['executive'] = fuzz.trimf(self.job_position.universe, [4, 5, 5])

        self.hotel_rating['three'] = fuzz.trimf(self.hotel_rating.universe, [3, 3, 4])
        self.hotel_rating['four'] = fuzz.trimf(self.hotel_rating.universe, [3, 4, 5])
        self.hotel_rating['five'] = fuzz.trimf(self.hotel_rating.universe, [4, 5, 5])

        self.salary_multiplier['very_low'] = fuzz.trimf(self.salary_multiplier.universe, [0.8, 0.8, 1.0])
        self.salary_multiplier['low'] = fuzz.trimf(self.salary_multiplier.universe, [0.9, 1.0, 1.2])
        self.salary_multiplier['medium'] = fuzz.trimf(self.salary_multiplier.universe, [1.1, 1.3, 1.5])
        self.salary_multiplier['high'] = fuzz.trimf(self.salary_multiplier.universe, [1.4, 1.6, 1.8])
        self.salary_multiplier['very_high'] = fuzz.trimf(self.salary_multiplier.universe, [1.7, 2.0, 2.0])

        # Creación de reglas difusas
        self.rules = [
            ctrl.Rule(self.job_position['junior'] & self.hotel_rating['three'], self.salary_multiplier['very_low']),
            ctrl.Rule(self.job_position['junior'] & self.hotel_rating['four'], self.salary_multiplier['low']),
            ctrl.Rule(self.job_position['junior'] & self.hotel_rating['five'], self.salary_multiplier['medium']),
            
            ctrl.Rule(self.job_position['mid'] & self.hotel_rating['three'], self.salary_multiplier['low']),
            ctrl.Rule(self.job_position['mid'] & self.hotel_rating['four'], self.salary_multiplier['medium']),
            ctrl.Rule(self.job_position['mid'] & self.hotel_rating['five'], self.salary_multiplier['high']),
            
            ctrl.Rule(self.job_position['senior'] & self.hotel_rating['three'], self.salary_multiplier['medium']),
            ctrl.Rule(self.job_position['senior'] & self.hotel_rating['four'], self.salary_multiplier['high']),
            ctrl.Rule(self.job_position['senior'] & self.hotel_rating['five'], self.salary_multiplier['very_high']),
            
            ctrl.Rule(self.job_position['executive'] & self.hotel_rating['three'], self.salary_multiplier['high']),
            ctrl.Rule(self.job_position['executive'] & self.hotel_rating['four'], self.salary_multiplier['very_high']),
            ctrl.Rule(self.job_position['executive'] & self.hotel_rating['five'], self.salary_multiplier['very_high']),
        ]

        self.salary_ctrl = ctrl.ControlSystem(self.rules)
        self.salary_simulation = ctrl.ControlSystemSimulation(self.salary_ctrl)

    def salary_calculator(self, job_position, stars, base_salary):
        """
        Calcula el salario final basado en el multiplicador difuso.

        Args:
            job_position (int): Nivel del puesto de trabajo (1-5).
            stars (int): Clasificación del hotel (3-5 estrellas).
            base_salary (float): Salario base del empleado.

        Returns:
            float: Salario final calculado.
        """
        
        self.salary_simulation.input['job_position'] = job_position
        self.salary_simulation.input['hotel_rating'] = stars

        self.salary_simulation.compute()

        salary = base_salary * self.salary_simulation.output['salary_multiplier']
        return salary
