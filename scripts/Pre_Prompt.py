from langchain.prompts import PromptTemplate

def Get_Prompt():
    prompt = PromptTemplate(
        input_variables=['context',"question"],
        template=
        """
            Tu es un assistant IT expert.
            Réponds UNIQUEMENT à partir du contexte ci-dessous.
            Si la réponse n'est pas dans le contexte, dis clairement :
            "Je ne trouve pas l'information dans le contexte fourni."

            Contexte:
            {context}

            Question:
            {question}

            Réponse:
        """
    )
    return prompt

if __name__ == "__main__":
    prompt = Get_Prompt()
    full_prompt = prompt.format(
        context="what is wydad athletic is the best club in the world",
        question="what is wydad atlathic club ?"
    )
    print(full_prompt)
