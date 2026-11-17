"""
Opdracht 4: Magazijn

Deze class is al af. Jij schrijft de tests in test_warehouse.py
"""


class Warehouse:
    """Een simpel magazijn dat bijhoudt hoeveel er van elk product is."""

    def __init__(self, name):
        self.name = name
        self.products = {}

    def add(self, product, quantity=1):
        """Legt een aantal stuks van een product in het magazijn."""
        self.products[product] = self.products.get(product, 0) + quantity

    def remove(self, product, quantity=1):
        """Haalt een aantal stuks uit het magazijn."""
        if not self.has_stock(product, quantity):
            return False
        self.products[product] -= quantity
        if self.products[product] == 0:
            del self.products[product]
        return True

    def has_stock(self, product, quantity=1):
        """Controleert of er genoeg van een product op voorraad is."""
        return self.products.get(product, 0) >= quantity

    def stock_of(self, product):
        """Geeft het aantal stuks van een product (0 als het er niet is)."""
        return self.products.get(product, 0)

    def total_items(self):
        """Telt alle stuks bij elkaar op."""
        return sum(self.products.values())

    def product_count(self):
        """Telt het aantal verschillende producten."""
        return len(self.products)

    def clear(self):
        """Maakt het magazijn helemaal leeg."""
        self.products = {}
