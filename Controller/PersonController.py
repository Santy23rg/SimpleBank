from abc import ABC, abstractmethod
from pathlib import Path
import sys

# Obtener la ruta del directorio actual
current_dir = Path(__file__).parent

# Construir la ruta relativa
model_path = current_dir / '../Model'

# Importar el módulo
sys.path.append(str(model_path))
from Person import *


class PersonController(Person, ABC):
    
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def search(self):
        pass
    
    @abstractmethod
    def update(self):
        pass