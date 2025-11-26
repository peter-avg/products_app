def get_prompt_for_tag_generation(context: str) -> str:
    return f"""
        You are an expert at generating product tags for e-commerce items.
        Generate a list of relevant and concise tags based on the following
        product description:
            {context}
    """
