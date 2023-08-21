import logging

logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('employee.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # Cambiar el logging por logger
        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Corey", "Schafer")
emp_3 = Employee("Jane", "Doe")
