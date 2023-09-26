from typing import List
import requests
from uagents import Context, Model, Protocol
# Use a pipeline as a high-level helper
from transformers import pipeline

class Category(Model):
    category: str

class News(Model):
    news: list

class registrationStatus(Model):
    status: str

class register(Model):
    country_code:str


news_proto = Protocol()


@news_proto.on_message(Category, replies=News)
async def send_news(ctx: Context, sender: str, cat:Category):
    
    pipe = pipeline("text-classification", model="elozano/bert-base-cased-news-category")
    country_code = ctx.storage.get("country")
    country_code = "in"
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=7cb246fcdbfd4eb2a9de837b56108226"
    response = requests.get(url)
    response_json = response.json()

    news_list = []

    ctx.logger.info("News fetched")
    for news in response_json['articles']:
        news_categories= get_category(news['title'])


        news_category = news_categories[0][0]['label']

        if news_category == cat.category:
            news_list.append(news)

        ctx.logger.info("Found Category")
    
    await ctx.send(sender, News(news=news_list))

@news_proto.on_message(register, registrationStatus)
async def send_registration_status(ctx: Context, sender: str, registration: register):
    ctx.storage.set("country", registration.country_code)
    ctx.storage.set("completed", 1)
    await ctx.send(sender, registrationStatus(status="Success"))


API_URL = "https://api-inference.huggingface.co/models/elozano/bert-base-cased-news-category"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

def get_category(input):
	output = query({
	"inputs": input,
    })

	return output
