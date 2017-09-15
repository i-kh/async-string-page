import random
import string


def get_random_str(length):
    """
    Form a string from uppercase letters, lowercase letters and digits
    :var length: length of the string
    :type length: str
    :return: String containing upper- and lowercase letters and digits
    :rtype: str
    """
    return ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits
    ) for x in range(16))

