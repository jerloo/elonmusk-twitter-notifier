
import time
from emailsender import send_mail


# Keywords to detect
keywords = ["stock", "share", "$", "doge", "crypto", "bitcoin"]


def tweet_engine(status):

    # if any(tweet in status.text.lower() for tweet in keywords) and status.user.id_str == "44196397":
    #     send_mail(f"Elon tweeted: {status.text} - on {time.ctime()}", False)

    if status.user.id_str == "44196397":
        send_mail(f"Elon tweeted: {status.text} - on {time.ctime()}", False)
    