'practice'

__author__ = 'Degelzhao'

sandwich_orders = ['chicken','pastrami','beef','pastrami','tuna','pastrami']
print('All the pastrami sandwiches has sold out!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('The following sandwiches are still selling:')
for sandwich_order in sandwich_orders:
    print(sandwich_order)