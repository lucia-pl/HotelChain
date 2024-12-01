from EmployeeSalary import EmployeeSalary

class Employee:
    """
    Represents an employee and calculates their monthly salary based on fuzzy logic
    defined in the EmployeeSalary class.
    """
    
    def __init__(self, id, hotel_rating, salary, job_position):
        """
        Initializes the employee's attributes.

        Args:
            id (int): Unique identifier for the employee.
            hotel_rating (int): Hotel's star rating (3-5 stars).
            salary (float): Base salary of the employee.
            job_position (int): Job position level (1-5).
        """
        self.id = id
        self.hotel_rating = hotel_rating
        self.salary = salary
        self.job_position = job_position
        
    def monthly_salary(self):
        """
        Calculates the employee's monthly salary adjusted by the fuzzy multiplier.

        Uses the EmployeeSalary class to determine the multiplier based on:
        - Job position level.
        - Hotel's star rating.

        Updates the employee's salary with the calculated value.

        Returns:
            None. Updates the `self.salary` attribute directly.
        """
        multiplier = EmployeeSalary()
        
        final_salary = multiplier.salary_calculator(self.job_position, self.hotel_rating, self.salary)
        
        self.salary = round(final_salary, 2)
