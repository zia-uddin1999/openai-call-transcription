import os
from dotenv import load_dotenv
from client import get_db_client, get_openai_client
from conversation_utils import generate_call_transcript, summarize_transcript, answer_questions
from file_utils import read_from_file, save_to_file
from user_conversational_history import get_user_conversational_history, set_user_conversational_history

load_dotenv() 

def main(): 
    openai_client = get_openai_client()
    db_client = get_db_client()
    
    while True:
        print("***********************************************************************************************")
        print("1. Generate a sales call transcript")
        print("2. Summarize the call transcript")
        print("3. Question & Answers")
        print("4. Quit")
    
        ip = input("> Choose an option: \n")
    
        # quit
        if ip == "4":
            break

        # generates a Sales call transcript and saves it to the file
        elif ip == "1":
            prompt = input("> Enter a prompt. Ex: Generate a sales call transcript between Sam from OpenAI and Satya from Microsoft \n")
            output_format = input("> Enter the format. Ex: HH:MM:SS Speaker (company website): Dialogue \n")
            language = input("> Enter a language. Ex: English, Spanish, etc \n")
    
            print("Generating the Transcript...")
            call_transcript = generate_call_transcript(openai_client, prompt, output_format, language)
    
            # saving the transcript to the file
            save_to_file(call_transcript)
            print(call_transcript)

        # summarizing the transcript
        elif ip == "2":
            transcript = read_from_file()
            language = input("> Enter a language. Ex: English, Spanish, etc \n")
    
            print("Summarizing the Transcript...")
            summary = summarize_transcript(openai_client, transcript, language)
            print(summary)

        # interactive Q&A over the transcript
        elif ip == "3":  
            username = os.environ["USER"]
            language = input("> Enter a language. Ex: English, Spanish, etc \n")
    
            # retrieving conversation history for the username
            conversations = get_user_conversational_history(db_client, username)
        
            # if no conversation history then add the transcript as the initial context
            if len(conversations) == 0:
                transcript = read_transcript_from_file()
                conversations = [{
                    "role": "system",
                    "content": f"You are an AI assistant. Provide helpful and concise answers to user questions conversationally in {language} for the context: {transcript}",
                }]

            # begins an interactive question & answer session and returns the conversation history
            conversations = answer_questions(openai_client, conversations, language)
    
            # saving the conversation under the username
            set_user_conversational_history(db_client, username, conversations)


# start 
main()