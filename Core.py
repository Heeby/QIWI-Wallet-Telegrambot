import time


def generate_code(user_id : str):
    """Generate code that user with user_id will add to transactions comments"""
    # TODO Add stenography because qiwi can ban users, that get money with strange comments
    # Do smth like that https://github.com/KuroLabs/stegcloak or https://www.youtube.com/watch?v=FYwPdfxUvMs
    return user_id + str(int(time.time()))[-7:]