import openai
import os
openai.api_key = os.getenv('OPEN_AI_API_KEY')

def aiInitPrompt(newsPrompt, marketPrompt, industry) :
  prompt = f'Could you please give a market analysis for the {industry} industry? \n'
  prompt += f'This is the current market stats : {marketPrompt}, and here are the news articles: {newsPrompt}'
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ],
    temperature=0.5,
  )
  print(completion)
  # return completion