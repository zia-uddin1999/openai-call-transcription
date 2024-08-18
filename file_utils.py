# save text to file
def save_to_file(transcript, file_name="transcript.txt"):
    with open(file_name, "w") as file:
        file.write(transcript)

# read text from file
def read_from_file(file_name="transcript.txt"):
    dialogues = []
    with open(file_name, "r") as file:
        dialogues.append(file.read())

    transcript = "\n".join(dialogues)
    return transcript
