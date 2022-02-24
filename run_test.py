import random

from main import actor
import run_int

random.seed(314)

# testing
testing_dialog = [
    ("hi", "Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?"),
    ]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = run_int.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
    print("test passed")


if __name__ == "__main__":
    run_test()
