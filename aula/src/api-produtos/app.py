from fastapi import FastAPI

from models.product import Product
from models.client import Client
from models.employee import Employee

app = FastAPI()

@app.get('/')
def say():
    return {'Fast': 'Hello'}

@app.get('/api/name/{name}') # endpoint
def say_hello(name:str):
    if not name:
        pass
    else:
        return {'Hello': name}

products = [
    Product(id=1, name='coca-cola', description='Refrigerante', price=9.98),
    Product(id=2, name='Tenis nike', description='Calçado', price=150.89),
    Product(id=3, name='Carro', description='Veiculo', price=9000.98),
]

@app.get('/api/products')
def get_products():
    return products

@app.get('/api/products/sale')
def get_sale():
    """
    Endpoitn que exibe o produco com maior desconto
    """
    return products[1]

clients = [
    Client(id=1, name='Maria', age=25, document='1635435132', address='Algum', phone='54654645678'),
    Client(id=2, name='Jose', age=52, document='41k463543k', address='Outro', phone='456546546'),
    Client(id=3, name='João', age=80, document='53u4u34', address='Por Aí', phone='45645637')
]

@app.get('/api/clients')
def get_clients():
    return clients

employee = [
    Employee(    
        name = 'Maria',
        age = 21,
        bithday = '10/12/2003',
        document = '13854643',
        address = 'qualquier' ,
        phone = '64113143532',
        salary = 1500,
        group = 'Escritorio',
        function = 'Estagiaria',
        initial_at = '01/04/2020',
        working = True,
        gender = 'Famale',
        height = 1.66,
        weight = 50,
        observations = 'sera promovida'
    ),
      Employee(    
        name = 'Marcio',
        age = 25,
        bithday = '10/01/1993',
        document = '315465453',
        address = 'outro' ,
        phone = '7435735432',
        salary = 3500,
        group = 'Produto',
        function = 'CLT',
        initial_at = '01/04/2020',
        working = True,
        gender = 'Male',
        height = 1.96,
        weight = 125,
        observations = 'Programador Junior'
    )
]

@app.get('/api/employee')
def get_employee():
    return employee