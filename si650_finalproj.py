from functions import *
import time

print('Welcome to Jokebox!')
time.sleep(1)

username = input('Enter your username: ')
while username == '':
	username = input('Please enter valid username: ')
check_user(username, df)

print('Please rate following 5 jokes from -10 to 10.')
time.sleep(1)


rating_dict = {}
joke_samples = get_sample_jokes(5)
joke_ids = joke_samples['joke_id'].tolist()
jokes = joke_samples['joke'].tolist()
ratings = []

for j in range(5):
	print('\n')
	rating = int(input(jokes[j]+'\n'+ 'your rating: '))
	while rating < -10 or rating > 10:
		rating = int(input('your rating is invalid. Rate between -10 and 10' +'\n'+ 'your rating: '))
	rating_dict[joke_ids[j]] = rating

#print(rating_dict)

rec_df =recommend(username, rating_dict)

for row in rec_df:
	print(row)
	time.sleep(1)
	rate = input('Was this joke to your taste?\nPlease rate!: ')
	print('\n')




