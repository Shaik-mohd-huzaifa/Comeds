from langchain.prompts import PromptTemplate


def DBPromptTemplate(table_details, user_query):
    templates = """
        Table and Id: {table_and_id}
    
        Query: {query}
    """

    prompt = PromptTemplate.from_template(template=templates)

    dbFormatedPrompt = prompt.format(
        table_and_id=table_details,
        query=user_query,
    )

    return dbFormatedPrompt
