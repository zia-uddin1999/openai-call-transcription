
# generates & returns the call transcript in the specified language
def generate_call_transcript(client, prompt, output_format, language):
    dialogue = [
        {
            "role": "system",
            "content": f"You are an AI assistant creating call transcripts in {language} with the format: {output_format}. Start directly with the conversation without any introductory messages.",
        },
        {"role": "user", "content": prompt},
    ]

    result = client.chat.completions.create(
        model="gpt-4o-0513", messages=dialogue, n=1, stop=None, temperature=0.7
    )

    transcript = result.choices[0].message.content
    return transcript

# returns the summary of the given transcript in the specified language
def summarize_transcript(client, transcript, language):
    response = client.chat.completions.create(
        model="gpt-4o-0513",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"You are a highly skilled AI trained in language comprehension and summarization in {language}. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points.",
            },
            {"role": "user", "content": transcript},
        ],
    )

    summary = response.choices[0].message.content
    return summary

# sets up an interactive Q&A sessions for the given context through conversations history
def answer_questions(client, conversations, language):
    while True:
        user_input = input("> Enter a question or type 'quit' to stop: ")
        if user_input == "quit":
            break

        question = {"role": "user", "content": user_input}
        conversations.append(question)

        response = client.chat.completions.create(
            model="gpt-4o-0513",
            temperature=0.7,
            messages=conversations,
            n=1,
            stop=None,
        )
        generated_answer = response.choices[0].message.content
        print("Answer: ", generated_answer)

        answer = {"role": "assistant", "content": generated_answer}
        conversations.append(answer)

    return conversations

