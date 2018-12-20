from km84.Croucer_Artem.workshop5.source.dataset.creater import create_dataset
import plotly
import plotly.graph_objs as go

dataset = create_dataset('')

user_product = dict()
for client in dataset:
    user_product[client] = set()
    for date in dataset[client]:
        user_product[client].update(set(dataset[client][date].keys()))
orders = list(user_product.values())
common_products_set = orders[0]
for order in orders:
    common_products_set = common_products_set.intersection(order)
print("Task 1: ", common_products_set)

from datetime import datetime

apple_date_price = dict()
for client in dataset:
    for date in dataset[client]:
        if 'apple' in dataset[client][date]:
            datetime_object = datetime.strptime(date, '%d.%m.%Y')
            apple_date_price[datetime_object] = dataset[client][date]['apple']['price']
print("Task 2: ", apple_date_price)
data = go.Scatter(x=list(apple_date_price.keys()), y=list(apple_date_price.values()))
plotly.offline.plot([data], filename='apple.html')

user_expenses = dict()
for client in dataset:
    user_expenses[client] = 0
    for date in dataset[client]:
        for product in dataset[client][date]:
            user_expenses[client] += float(dataset[client][date][product]['price']) * float(
                dataset[client][date][product]['quantity'])
print("Task 3: ", user_expenses)
data = go.Bar(x=list(user_expenses.keys()), y=list(user_expenses.values()))
plotly.offline.plot([data], filename='user_expenses.html')

product_popularity = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            if product not in product_popularity:
                product_popularity[product] = 0
            product_popularity[product] += float(dataset[client][date][product]['quantity'])
products = list(product_popularity.keys())
quantities = list(product_popularity.values())
max_quantities = max(quantities)
min_quantities = min(quantities)
index_max = quantities.index(max_quantities)
index_min = quantities.index(min_quantities)
print("Task 4: ", product_popularity, products[index_max], products[index_min])

product_price = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            product_price[product] = float(dataset[client][date][product]['price'])
products = list(product_price.keys())
prices = list(product_price.values())
max_price = max(prices)
index_max = prices.index(max_price)
print("Task 5: ", products[index_max], max_price)

product_user = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            if product not in product_user:
                product_user[product] = 0
            product_user[product] += 1
data = go.Bar(x=list(product_user.keys()), y=list(product_user.values()))
plotly.offline.plot([data], filename='product_user.html')

import sys

input_file = 'data/orders.csv'
out_file = 'data/orders_out.csv'
try:
    with open(input_file, 'r') as f:
        file_content = f.read()
        print("read file " + input_file)
    if not file_content:
        print("no data in file " + input_file)
        file_content = "out data..."
    with open(out_file, 'w') as dest:
        dest.write(file_content)
        print("wrote file " + out_file)
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except:  # handle other exceptions such as attribute errors
    print("Unexpected error:", sys.exc_info()[0])
