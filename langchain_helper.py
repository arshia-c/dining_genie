import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
load_dotenv(find_dotenv())
KEY = os.environ["OPENAI_API_KEY"]

llm=OpenAI(openai_api_key=KEY,temperature=0.6)

def generate_restaurant_name(cuisine,no_of_people,meal,budget,loaction):
    prompt_template_name=PromptTemplate(
        input_variables=['cuisine','no_of_people','meal','budget','loaction'],
        template="Suggest top 5 restaurants of {cuisine} cuisine where {no_of_people} number of people are going for {meal} and having a of {budget} Indian rupees as budget in {location} location."  
    )
    llm_chain=LLMChain(llm=llm,prompt=prompt_template_name,verbose=True)

    output=llm_chain.run(cuisine=cuisine,no_of_people=no_of_people,meal=meal,budget=budget,location=loaction)

    return output