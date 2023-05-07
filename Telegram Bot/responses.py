def sample_responses(input_text):
    text = str(input_text).lower()

    if(input_text) in ("hello", "hi", "hey"):
        return "Hey how can I help you?"
    
    if(input_text) in ("who", "who are you"):
        return "I'm busybee's bot"

    return "I don't understand you"
