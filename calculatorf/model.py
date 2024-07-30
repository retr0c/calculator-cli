class Calculator:
    
    def add(self, numero1: float, numero2: float) -> float:
        return numero1 + numero2
    
    def subtract(self, numero1: float, numero2: float) -> float:
        return numero1 - numero2
    
    def multiply(self, numero1: float, numero2: float) -> float:
        return numero1 * numero2
    
    def divide(self, numero1: float, numero2: float) -> float :
        if numero2 == 0:
            return "Cannot divide by 0!"
        
        return numero1 / numero2
    
    