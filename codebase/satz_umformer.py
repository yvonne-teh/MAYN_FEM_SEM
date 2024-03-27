import asyncio
from openai import AsyncOpenAI
from semeval_reader import entries as semeval_tuples

client = AsyncOpenAI()


async def main(semeval_tuple):
    # Your existing setup
    system = """
    Find the verb of the sentence that describes the relation between the nouns e1 and e2 and return its lemma.
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


def extract_verb(sentence):
    # remove to, 3rd person s, ing...
    if sentence[0:3] == 'to ':
        return sentence[3::]
    if sentence[-1] == 's':
        return sentence[0:-1]
    if sentence[-3:] == 'ing':
        # test for double consonants before ing:
        validate = sentence[-5:-3]
        if validate[0] == validate[1]:
            # remove one consonant
            sentence = sentence[:-4] + sentence[-3:]
        return sentence[:-3]
    return sentence


# tests
def test_stemmer():
    print(extract_verb("to swim"))
    print(extract_verb("swim"))
    print(extract_verb("tolerate"))
    print(extract_verb("swims"))
    print(extract_verb("hissing"))


print(len(semeval_tuples))
verb_dict = dict()

# get verb dict
try:
    for tuple in semeval_tuples:

        data = asyncio.run(main(tuple))
        if data == 'fail!!':
            continue

        print(f"\nSatz: {tuple['sentence']}")
        print("GPT : " + data + "\n")
        verb = extract_verb(data)

        # don't put wrongly returned sentences by GPT in the dict
        if ' ' in verb:
            continue

        try:
            verb_dict[verb] += 1
        except:
            verb_dict[verb] = 1
except KeyboardInterrupt:
    pass


print(verb_dict)
