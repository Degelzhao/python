'practice'

__author__ = 'Degelzhao'

sandwich_orders = ['chicken','beef','tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your %s sandwich' % current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

print('All the sandwiches are ready!')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
