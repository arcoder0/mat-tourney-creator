from datetime import datetime, timezone, date
import requests
import time
import os

name = "Cash Tournament Qualifier50USD"

description = '''Winner will qualify for 50 USD cash tmt- lichess.org/swiss/ySQgdBPY
Next Cash Tournament Qualifier-
lichess.org/team/mixailov_alex_team/tournaments
Please save the tournament link!
Join 26$ tournament: https://lichess.org/swiss/11gwngOe
Join 18$ tournament: https://lichess.org/swiss/o3fiVhPB
Sign up for classes with a professional trainer, buy a book: TG @Viktortahirov
TG channels: https://t.me/korolevskayalogika
https://t.me/chesskaissa'''

token = os.getenv('LICHESS_TOKEN')

hours = (1, 3, 5, 7, *range(8, 22), 23)
controls = ((10, 0), (10, 5), (7, 2), (1, 0), (5, 0), (3, 0), (3, 1), (5, 2), (3, 2), (10, 0), (10, 5), (7, 2), (1, 0), (5, 0), (3, 0), (3, 1), (5, 2), (5, 2), (3, 2))
today = date.today()

for i in range(len(hours[7:])):
	time.sleep(5)

	hour = hours[i]
	control = controls[i]

	# Year, month, day, hour, minute, second
	start_date = (2025, 9, today, hour, 0, 0)
	start_date = datetime(*start_date, tzinfo=timezone.utc)
	start_date_sec = int(start_date.timestamp()) * 1000
	print(start_date_sec)

	headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
	
	config = {
		"teamId": "mixailov_alex_team",
		"name": name,
		"clock.limit": control[0] * 60,
		"clock.increment": control[1],
		"nbRounds": 7,
		"startsAt": start_date_sec,
		"description": description,
		"conditions.playYourGames": True
		}

	try:
		response = requests.post( 
	            f"https://lichess.org/api/swiss/new/mixailov_alex_team",
	            headers=headers,
	            json=config
	        )
		print(response.status_code)
		if response.status_code != 200:
			print(response.text)

	except Exception as e:
		print(e)
		continue