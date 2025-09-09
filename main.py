from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from ice_breaker.agents.linkedin_lookup_agent import lookup as linkedin_lookup
from ice_breaker.agents.twitter_lookup_agent import lookup as twitter_lookup
from ice_breaker.third_parties.linkedin import scrape_linkedin_profile
from ice_breaker.third_parties.twitter import scrape_user_tweets
from output_parsers import summary_parser, Summary
from typing import Tuple


def ice_breaker_with(name: str) -> Tuple[Summary, str]:
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
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_data", "tweets"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()},
    )

    # Do NOT set temperature
    llm = ChatOpenAI(model="gpt-5-nano", max_retries=3)
    chain = summary_prompt_template | llm | summary_parser
    result: Summary = chain.invoke(input={
        "linkedin_data": linkedin_data,
        "tweets": tweets,
    })

    print("Result:", result)
    print("*" * 20)
    print("Summary:", result.summary)
    print("Facts:", result.facts)

    return result, linkedin_data.get("photoUrl", "")

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_breaker_with(name="Harrison Chase")
