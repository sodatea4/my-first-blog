name = 'Heather'
if name == 'Heather':
    print('Hey Heather!')
elif name == 'Potato':
    print('Hey Potato!')
else:
    print('Hey anonymous!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()
def hi(name):
    print('Hi ' + name + '!')
girls = ['Abigail', 'Alica', 'Grace', 'Pierce', 'Heather']
for name in girls:
    hi(name)
    print('Next girl')
