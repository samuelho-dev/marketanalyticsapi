import openai
import os

openai.api_key = os.getenv("OPEN_AI_API_KEY")


def ai_init_prompt(newsPrompt, marketPrompt, industry):
    prompt = f"Give a market analysis for the {industry} industry analyze and highlight the key points and sentiments. Apply specificity to the backgrounds of the publisher, author and time of posting in relation to the sentiments of the global economy. \n"
    prompt += f"This is the current market stats : {marketPrompt}, and here are the news articles: {newsPrompt}"

    completion = start_prompt(prompt)

    return completion


def start_prompt(prompt):
    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    if completion.choices:
        message = completion.choices[0].text
    else:
        message = "Error: No response from GPT-3 API"

    return message


def continue_prompt(prompt):
    completion = openai.Completion.create(
        model="davinci",
        prompt=prompt,
        temperature=0.5,
    )

    if completion.choices:
        message = completion.choices[0].text
    else:
        message = "Error: No response from GPT-3 API"

    return message
