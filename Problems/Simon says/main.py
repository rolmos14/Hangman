def what_to_do(instructions):
    me = "I "
    keyphrase = "Simon says"
    if instructions.startswith(keyphrase):
        return me + instructions.replace(keyphrase + " ", "")
    elif instructions.endswith(keyphrase):
        return me + instructions.replace(" " + keyphrase, "")
    else:
        return me + "won't do it!"
