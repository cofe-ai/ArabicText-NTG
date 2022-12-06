from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument("--pred", required=True)
    parser.add_argument("--gold", required=True)
    parser.add_argument("--metrics", default=["rouge", "bleu"], nargs="+")
    args = parser.parse_args()
    return args