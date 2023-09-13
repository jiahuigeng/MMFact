import openai

openai.api_key = "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" # fill your openai api key

def chatgpt(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a NLP expert that is good at fact checking. You will be presented with claims, evidence, and the corresponding output. Your task is to determine whether the claim is supported, refuted, or NEI (not enough information) based on the provided evidence.\n\nInput 1:\nClaim: Some registered Democratic Party voters in Alaska and Florida received emails U.S.\nEvidence: Unlike the U.S., Iran does not interfere in other country's elections. The world has been witnessing U.S.' own desperate public attempts to question the outcome of its own elections at the highest level.1/2 https://t.co/8AOKvIZr1h - Alireza Miryousefi (@miryousefi) October 22, 2020\nOutput 1: supported\n\nInput 2:\nClaim: 'No one has died of cancer or heart disease since the COVID-19 thing started.\nEvidence: COVID-19 was the third leading cause of death after cancer and heart disease in 2020 in the United States, according to provisional federal mortality data.\nOutput 2: refuted\n\nInput 3:\nClaim: U.S. Sen. Elizabeth Warren's presidential campaign claimed in October 2019 that Facebook CEO Mark Zuckerberg had endorsed President Donald Trump for re-election.\nEvidence: Breaking news: Mark Zuckerberg and Facebook just endorsed Donald Trump for re-election. You're probably shocked, and you might be thinking 'How could this possibly be true?' Well, it's not. (Sorry). But what Zuckerberg *has* done is given Donald Trump free rein to lie on his platform - and then to pay Facebook gobs of money to push out their lies to American voters. If Trump tries to lie in a TV ad, most networks will refuse to air it. But Facebook just cashes Trump's checks. Facebook already helped elect Donald Trump once. Now, they're deliberately allowing a candidate to intentionally lie to the American people. It's time to hold Mark Zuckerberg accountable - add your name if you agree.\nOutput 3: NEI \n your output only needs to provide one of supported, refuted, or NEI, don't need to add 'output:'"},
                {"role": "user", "content": user_input},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result

def davinci(prompt):
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response

if __name__ == "__main__":
    prompt = "Claim: Actor Jessica Walter was the voice of Fran Sinclair in the TV show 'Dinosaurs. Evidence: Just learned that Jessica Walter was also Fran Sinclair on Dinosaurs. Absolute legend https://t.co/x0vf8K5HUd — Mike Drucker (@MikeDrucker) March 25, 2021."
    print(chatgpt(prompt))