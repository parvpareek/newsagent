from protocols.protocol import *

from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
 
NEWS_ADDRESS = "agent1qgyewt0ypuxtm7qn9r3ehq56rrfcza447uz7hutqtxm4uzs2v32zwv2axf8"
 
user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)
 
fund_agent_if_low(user.wallet.address())
 
country = input("enter your coutnry code in two letter ISO format(e.g in, us)")


registration = register(
    country_code = country
)


 
# This on_interval agent function performs a request on a defined period
@user.on_interval(period=30, messages=register)
async def interval(ctx: Context):
    completed = ctx.storage.get("completed") or 0
 
    if not completed:
        await ctx.send(NEWS_ADDRESS, registration)
 
@user.on_message(registrationStatus, replies=Category)
async def handle_registration_response(ctx: Context, sender: str, msg: Category):
    
    print("Enter the category you want your news from 1. World 2. Automobile 3.Science 4. Entertainment 5. Sports 6. Technology 7. Politics")
    category = input("Enter your choice")
    await ctx.send(NEWS_ADDRESS, Category(category=category))
 
@user.on_message(News)
async def handle_news(ctx: Context, _sender: str, news: News):
    ctx.logger.info("The news is: ")
    for article in news:
        ctx.logger.info(article['title'])
        ctx.logger.info(article['description'])

        ctx.logger.info("--"*20)



 
if __name__ == "__main__":
    user.run()