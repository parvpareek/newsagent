from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from protocols.protocol import news_proto
 
news_agent = Agent(
    name="news_agent",
    port=8001,
    seed="news secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(news_agent.wallet.address())
 
print(news_agent.address)
news_agent.include(news_proto)
 
if __name__ == "__main__":
    news_agent.run()