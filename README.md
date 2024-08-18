### Approach:

#### Task 1: Generating Call Transcripts
1. Consulted the OpenAI documentation for using OpenAI models and appropriate APIs.
2. Experimented with various prompts and client parameters to generate call transcripts.
3. Incorporated multi-language support by adding language context.
4. Implemented file read and write operations.
5. Saved the generated transcripts to files.

#### Task 2: Summarizing Call Transcripts
1. Consulted the OpenAI documentation for using OpenAI models and appropriate APIs.
2. Experimented with various prompts and client parameters to generate transcript summaries.
3. Incorporated multi-language support by adding language context.
4. Read stored transcripts from files and performed summarization using the models.

#### Task 3: Answering Questions
1. Consulted the OpenAI documentation for using OpenAI models and appropriate APIs.
2. Experimented with various prompts and client parameters to generate answers to user questions.
3. Incorporated multi-language support by adding language context.
4. Read user questions via prompts and generated answers using the models.
5. Stored the user's conversational history in MongoDB.

#### Unit Testing:
- Developed unit tests for core utilities such as `generate_call_transcript`, `summarize_transcript`, and `answer_questions`.

### Resources
- OpenAI API: [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)

### Steps to Run

1. To run the program, set the following environment variables for OpenAI and MongoDB access:
    ```
    AZURE_OPENAI_API_KEY=""
    AZURE_OPENAI_ENDPOINT=""
    OPENAI_API_VERSION=""
    USER=""
    PASSWORD=""
    ```

2. Execute the script:
    ```sh
    $ python main.py
    ```

3. Sample output: Click to watch.
    [Video](./output.mp4)

### Running Unit Tests

- Execute the unit tests:
    ```sh
    $ python conversation_utils_test.py
    ```

---

This version provides clear and detailed instructions while maintaining the original intent and structure.