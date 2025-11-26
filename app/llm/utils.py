from .config import CLIENT, MODEL
from .prompts import get_prompt_for_tag_generation
from ..schemas import TagResponse


def get_tags(content: str) -> TagResponse:
    response = CLIENT.chat.completions.parse(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": get_prompt_for_tag_generation(content)
            }
        ],
        response_format=TagResponse
    )

    tags = response.choices[0].message

    if tags.refusal:
        raise ValueError("Tag generation was refused by the model.")


    print(tags.parsed)

    return tags.parsed
