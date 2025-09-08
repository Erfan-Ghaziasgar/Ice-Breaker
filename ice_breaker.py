from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from ice_breaker.agents.linkedin_lookup_agent import lookup as linkedin_lookup
from ice_breaker.third_parties.linkedin import scrape_linkedin_profile

from ice_breaker.agents.twitter_lookup_agent import lookup as twitter_lookup
from ice_breaker.third_parties.twitter import scrape_user_tweets


def ice_breaker_with(name: str) -> str:
    linkedin_profile_url = linkedin_lookup(name=name)
    print(f"Linkedin Profile URL: {linkedin_profile_url}")

    twitter_username = twitter_lookup(name=name)
    print(f"Twitter Username: {twitter_username}")

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url, mock=False
    )

    tweets = scrape_user_tweets(
        username=twitter_username, num_tweets=5, mock=False)

    summary_template = """
    given the information about a person from linkedin {linkedin_data},
    and their latest twitter posts {tweets} I want you to create:
    1. A short summary
    2. two interesting facts about them

    Use both information from twitter and Linkedin
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_data", "tweets"],
        template=summary_template,
    )

    # Do NOT set temperature
    llm = ChatOpenAI(model="gpt-5-nano", max_retries=3)
    chain = summary_prompt_template | llm
    result = chain.invoke(input={
        "linkedin_data": linkedin_data,
        "tweets": tweets,
    })
    return result.content


if __name__ == "__main__":
    load_dotenv()

    print("Enter the full name of the person you want to break the ice with:")
    name = input().strip()
    ice_breaker_message = ice_breaker_with(name)
    print(f"Ice Breaker Message:\n{ice_breaker_message}")
