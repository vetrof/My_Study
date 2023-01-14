# Hello!
# reference:
# Hello - $0
# Hello, Newman - $0
# How you doing? - $20
# What's happening? - $100

# test area
# user_input = 'Hello'.lower().strip()
# user_input = 'Hello, Newman'.lower().strip()
# user_input = 'How you doing?'.lower().strip()
# user_input = "What's happening?".lower().strip()


user_input = input('Greeting: ').lower().strip()

if 'hello' in user_input:
    print('$0')
elif user_input[0] == 'h':
    print('$20')
else:
    print('$100')

