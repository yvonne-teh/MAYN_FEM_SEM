import asyncio
from openai import AsyncOpenAI
from semeval_reader import entries as semeval_tuples

client = AsyncOpenAI()


async def main(semeval_tuple):
    # Your existing setup
    system = """
    Replace the third word with the [MASK] token.
    """

    prompt = semeval_tuple['sentence']

    try:
        # Set a timeout for the request
        chat_completion = await asyncio.wait_for(
            client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                model="gpt-3.5-turbo-0125",
            ),
            timeout=10.0  # Timeout in seconds
        )
        return chat_completion.choices[0].message.content
    except asyncio.TimeoutError:
        # Handle the case where the request takes too long
        print("Request timed out. Skipping...")
        return 'fail!!'  # Or any other fallback action


# get verb dict
try:
    for tuple in semeval_tuples:

        data = asyncio.run(main(tuple))
        if data == 'fail!!':
            continue

        print(f"\nSatz: {tuple['sentence']}")
        print("GPT : " + data + "\n")

except KeyboardInterrupt:
    pass

