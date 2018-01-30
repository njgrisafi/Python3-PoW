import string
import random
import hashlib
import time


config = {
    "challenge": '7kas74jSfejGJ54SfjX5gZ111w',
    "size": 25,
    "resulting_zeros": "0000",
    "shaHash": hashlib.sha256()
}


def generate_answer_attempt(challenge=config["challenge"], size=config["size"]):
    answer = ''.join(
        random.choice(string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits) for x in range(size)
        )
    attempt = challenge + answer
    return answer, attempt


def proof_of_work(shaHash=config["shaHash"]):
    while True:
        answer, attempt = generate_answer_attempt()
        shaHash.update(attempt.encode())
        solution = shaHash.hexdigest()
        if(solution.startswith(config["resulting_zeros"])):
            return answer


if __name__ == "__main__":
    start = time.time()
    answer = proof_of_work()
    stop = time.time()
    print("Challenge: {0}".format(config["challenge"]))
    print("Difficulty: {0}".format(config["resulting_zeros"]))
    print("Answer: {0}".format(answer))
    print("Solved in {0} seconds".format(stop - start))
