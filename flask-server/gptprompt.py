import openai
import os

openai.api_key = os.getenv("OPEN_AI_API_KEY")


def aiInitPrompt(newsPrompt, marketPrompt, industry):
    prompt = f"Give a market analysis for the {industry} industry analyze and highlight the key points and sentiments. Apply specificity to the backgrounds of the publisher, author and time of posting in relation to the sentiments of the global economy. \n"
    prompt += f"This is the current market stats : {marketPrompt}, and here are the news articles: {newsPrompt}"

    completion = startPrompt(prompt)

    return completion


def startPrompt(prompt):
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


def continuePrompt(prompt):
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
