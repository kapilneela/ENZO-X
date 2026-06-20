from core.memory import Memory

memory = Memory()


def process(user_input):

    text = user_input.lower().strip()


    # Existing name memory
    if "my name is" in text:

        name = text.split("my name is")[1].strip()

        memory.remember("username",name)

        return f"I'll remember your name as {name}"


    if "who am i" in text:

        name = memory.recall("username")

        if name:
            return f"You are {name}"

        return "I don't know yet."


    # Generic learning:
    # remember X is Y

    if text.startswith("remember"):

        try:

            statement = text.replace("remember","").strip()

            key,value = statement.split(" is ",1)

            key=key.strip()

            value=value.strip()

            memory.remember(key,value)

            return f"I'll remember that {key} is {value}"

        except:

            return "Use: remember X is Y"


    # Generic recall:
    # what is X

    if text.startswith("what is"):

        key = text.replace("what is","").strip()

        value = memory.recall(key)

        if value:

            return f"{key} is {value}"



    # Generic recall:
    # what is my X

    if text.startswith("what is my"):

        key = text.replace("what is my","").strip()

        value=memory.recall(key)

        if value:

            return f"Your {key} is {value}"


    return None