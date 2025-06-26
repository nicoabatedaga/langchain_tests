from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Instanciar el modelo
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Crear el prompt template
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")])

chain = prompt | llm


def ejecutar_chatbot():
    print("Bienvenido(a) a mi chatbot con LangChain. Escribe 'salir' para terminar.")
    # Lista para mantener el historial de la conversación
    chat_history = []

    while True:
        # Obtenemos la entrada del usuario
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chatbot: ¡Hasta luego!")
            break

        # Generamos la respuesta
        response = chain.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response.content))

        print(f"Chatbot: {response.content}")


if __name__ == "__main__":
    ejecutar_chatbot()
