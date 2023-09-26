# News Agent

## Dependencies
uAgents

## Explanation

Protocols file contains all the protocols used to ommunicate between the agents. The user sends a registration request to register the country of the user and teh agent then returns a registration status. If the registration status is successful a category request is sent to the news agent and the news agent fetches all the latest headlines and divvides the news using a transformer model api(i didnt have time to train one) and filters the ones in the category the user needs. The news agent returns a list of news of that category. 