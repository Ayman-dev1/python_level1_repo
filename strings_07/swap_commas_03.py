# program to swap commas and dots in a string

statement = 'He is Ahmed, Ahmed lives in cairo, Ahmed Plays Football.'

statement = statement.replace(',', '*')
statement = statement.replace('.', ',')
statement = statement.replace('*', '.')
print(statement)
