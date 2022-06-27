
from email import message
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = "STOCK_API"
NEWS_API = "NEWS_API"
twilio_sid = "twilio_sid"
twilio_auth_token = "twilio_auth_token"
twilio_phone_number = "twilio_phone_number"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)



day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
updown = None
if difference > 0:
    updown = "🔼"
else:
    updown ="🔽"



#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)


#If TODO4 percentage is greater than 5 then print("Get News").

if abs(diff_percent) > 5:
    news_params = {
        "apikey": NEWS_API,
        "searchIn": "title",
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articels =news_response.json()["articles"]
    


#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

top_tree_articles = articels[:3]
print(top_tree_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.
formatted_artilce_list =  [f"{STOCK_NAME}: {updown}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in top_tree_articles]

#Send each article as a separate message via Twilio. 
client = Client(twilio_sid, twilio_auth_token)
for article in formatted_artilce_list:
    message = client.messages.create(
        body=article,
        from_=twilio_phone_number,
        to="Your Phone Number"
    )


