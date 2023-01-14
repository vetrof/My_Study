text = 'здравсвтвуй жопа новый год$'
lists = text.split()
words = [i for i in lists if i.isalnum() == True]
wordf = ' '.join(words)
print(wordf)



original_prices = [100, 200, 500, 1100]
discount = 0.15  # 15%
new_prices = [i * (1 - discount) for i in original_prices]
print(new_prices)


text = 'Сколько лет, сколько зим'
parts = ['*' if i == 'о' else i for i in text]
new_text = ''.join(parts)
print(new_text)



