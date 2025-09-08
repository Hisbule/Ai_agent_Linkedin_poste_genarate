import ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama as LangOllama


def generate_linkedin_post(topic: str, language: str):
    """
    Generate a professional LinkedIn post using Gemma 3 (via Ollama).
    """
    prompt_template = PromptTemplate(
        input_variables=["topic", "language"],
        template=""" Write a professional LinkedIn post about {topic}.
        The post should be 2–4 paragraphs long, engaging, and written in {language}."""
    )

    llm = LangOllama(model="gemma3:4b")

    linkedin_post_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )

    try:
        response = linkedin_post_chain.invoke({
            "topic": topic,
            "language": language
        })
        return response["text"]
    except Exception as e:
        return f" Error generating LinkedIn post: {e}"


def embed_post(text: str):
    """
    Generate embeddings locally using Ollama’s nomic-embed-text model.
    """
    try:
        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=text
        )
        return response["embedding"]
    except Exception as e:
        print(f" Error generating embeddings: {e}")
        return []


if __name__ == "__main__":
    topic = input("Enter the topic of your LinkedIn post: ")
    language = input("Enter the language (e.g., English, Bengali, Spanish): ")

    post = generate_linkedin_post(topic, language)
    print("\n Generated LinkedIn Post:\n")
    print(post)

    if not post.startswith(""):
        print("\n🔎 Generating embeddings with Ollama...")
        embedding_vector = embed_post(post)
        if embedding_vector:
            print(f" Embedding vector generated locally!")
            print(f"Length: {len(embedding_vector)}")
            print(f"First 10 values: {embedding_vector[:10]}")
