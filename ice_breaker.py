from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from ice_breaker.agents.linkedin_lookup_agent import lookup
from ice_breaker.third_parties.linkedin import scrape_linkedin_profile


def ice_breaker_with(name: str) -> str:
    linkedin_profile_url = lookup(name)
    print(f"Linkedin Profile URL: {linkedin_profile_url}")

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url, mock=False
    )

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary of the person in less than 50 words.
    2. Two interesting facts about the person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # Do NOT set temperature
    llm = ChatOpenAI(model="gpt-5-nano", max_retries=3)
    chain = summary_prompt_template | llm
    result = chain.invoke(input={"information": linkedin_data})
    return result.content


if __name__ == "__main__":
    load_dotenv()

    print("Enter the full name of the person you want to break the ice with:")
    name = input().strip()
    ice_breaker_message = ice_breaker_with(name)
    print(f"Ice Breaker Message:\n{ice_breaker_message}")
