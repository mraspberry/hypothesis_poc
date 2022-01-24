import argparse
from hypothesis_poc import divrem


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numerator", type=int, help="Numerator")
    parser.add_argument("divisor", type=int, help="Divisor")
    args = parser.parse_args()

    print(
        "Quotient: {} Remainder: {}",
        format(*divrem.divrem(args.numerator, args.divisor)),
    )


if __name__ == "__ main__":
    main()
