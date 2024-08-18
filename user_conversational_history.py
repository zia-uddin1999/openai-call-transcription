# return the conversation history for the given user
def get_user_conversational_history(client, username):
    db = client.sales_call_transcript
    collection = db.answer_questions

    query = {"username": username}
    for document in collection.find(query):
        if document["conversations"] != None and len(document["conversations"]) > 0 :
            return document["conversations"]
    return []


# sets the conversation history under the given user
def set_user_conversational_history(client, username, conversations):
    if conversations != None and len(conversations) > 0 :
        db = client.sales_call_transcript
        collection = db.answer_questions
    
        query = {"username": username}
        question_answers = {
            "$set": {
                "conversations": conversations
            }, 
            "$setOnInsert": {
                "username": username,
            }
        }
    
        # Insert the user's conversation into the collection
        collection.update_one(query, question_answers, upsert=True)