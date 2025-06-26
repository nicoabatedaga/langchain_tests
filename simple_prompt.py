from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Instanciar el modelo
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

template = PromptTemplate(
    input_variables=["tema"],
    template="Explica brevemente y de forma sensilla el siguiente tema: {tema}"
)


def explicar_tema(tema):
    prompt = template.format(tema=tema)
    respuesta = llm.invoke(prompt)
    return respuesta.content


if __name__ == "__main__":
    response = explicar_tema("historia de lamborghini")
    print(response)
