class CartePizzeriaException(Exception):
    pass

class Pizza:
    def __init__(self, nom, ingredients, prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

class CartePizzeria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self,pizza):
        return self.pizzas.append(pizza)
    
    def remove_pizza(self,name):
        for pi in self.pizzas:
            if pi.nom == name:
                self.pizzas.remove(pi)
                return
            raise CartePizzeriaException(name)
