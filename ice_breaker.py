from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedIn import scrape_linkedin_profile

if __name__ == "__main__":
    summary_template = """
      Given the information {information} about a person from I want you to create:
      1. a short summary
      2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # linkedin_data = scrape_linkedin_profile(
    #     linkedin_profile_url='https://www.linkedin.com/in/soonkwon-hwang-22390a178/')
    linkedin_data = scrape_linkedin_profile(name="eden-marco")

    print(chain.run(information=linkedin_data))
