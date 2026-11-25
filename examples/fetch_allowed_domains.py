from browserbase import BadRequestError

from examples import bb


def run() -> None:
    # A host on the list (or a subdomain of one) is fetched as usual.
    page = bb.fetch_api.create(
        url="https://example.com/",
        allowed_domains=["example.com"],
    )
    print(f"Fetched {page.status_code} from example.com")

    # Any other host, or a redirect to one, is rejected with a 400 before it is reached.
    try:
        bb.fetch_api.create(
            url="https://example.com/",
            allowed_domains=["example.org"],
        )
    except BadRequestError as error:
        print(f"Blocked: {error.message}")


if __name__ == "__main__":
    run()
