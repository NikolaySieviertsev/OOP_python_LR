"""
Task 1.
Create a class that describes a Product of online store. As a Product fields you can use a price,
description and product' dimensions.
Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
Create a class that describes an Order.
- the order must contain data about the customer who carried it out and products.
Implement a method for calculating the total order value.
"""


class Product(object):

    def __init__(self, price, description, dimensions):
        if not isinstance(price, (int, float)) and isinstance(dimensions, (int, float)):
            raise TypeError("Incorrect type of price or/and dimensions!")
        if price < 0 or dimensions <= 0:
            raise ValueError('Price has to be a positive value and/or dimensions cannot have negative or zero value!')
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product: price - {self.price}, description - {self.description}, dimensions - {self.dimensions})"


class Customer(object):

    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f"Customer({self.surname}, {self.name}, {self.patronymic}, {self.mobile_phone})"


class Order(object):

    def __init__(self, customer, **kwargs):
        if not all(kwargs):
            raise TypeError("Selected product have to belong to 'Product' type and cannot be empty!")
        if not (isinstance(customer, Customer)):
            raise TypeError("New customer have to belong to 'Customer' type!")
        self.__selected_products = kwargs
        self.__new_customer = customer

    def get_total_price(self):

        total = 0
        for element in self.__selected_products:
            total += self.__selected_products[element].price * self.__selected_products[element].dimensions
        return total

    def __str__(self):
        return "\tCurrent order:\nCustomer:\t{surname} {name} {patronymic}\nFinal price:\t{price}$".format(
            surname=self.__new_customer.surname,
            name=self.__new_customer.name,
            patronymic=self.__new_customer.patronymic,
            price=self.get_total_price())


fresh_customer = Customer("Severtsev", "Kolya", "Serhiiovich", 380632110359)
product_1 = Product(22, "apples", 4)
product_2 = Product(15, "keyboards", 12)
product_3 = Product(10, "keyboards", 3)
product_4 = Product(1, "keyboards", 48)
order = Order(fresh_customer, product1=product_1, product2=product_2, product3=product_3, product4=product_4)
print(order)

# print(product_1)
# print(fresh_customer)
