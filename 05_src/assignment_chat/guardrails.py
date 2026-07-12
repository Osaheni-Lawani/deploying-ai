def check_input(question):
    """
    Check whether the input contains blocked topics.
    """

    if question is None:
        return False

    blocked_words = [
        "Cats or dogs",
        "Horoscopes or Zodiac Signs",
        "Taylor Swift"
    ]

    for word in blocked_words:
        if word.lower() in question.lower():
            return False

    return True


def validate_input(question):
    """
    Validate user input before sending it to the RAG pipeline.
    """

    if question is None:
        return False, "Please enter a question."

    if len(question.strip()) == 0:
        return False, "Please enter a valid question."

    if len(question) > 1000:
        return False, "Question is too long."

    if not check_input(question):
        return False, "This topic is outside the scope of this assistant."

    return True, ""


def validate_output(answer):
    """
    Validate generated responses before returning them.
    """

    if answer is None or len(answer.strip()) == 0:
        return "No answer was generated."

    return answer
