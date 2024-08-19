from pathlib import Path
from abc import ABC, abstractmethod
import sys

current_dir = Path(__file__).parent

model_path = current_dir / '../Model'

sys.path.append(str(model_path))

from Service import *

class ServiceController(Service, ABC):
    
    @abstractmethod
    def register(self):
        pass
    