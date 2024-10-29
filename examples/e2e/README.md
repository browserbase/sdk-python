# End-to-end tests

This directory contains end-to-end tests that run against a real Browserbase instance.

## Running the tests

To run the tests, you will need to set the following environment variables:

- `BROWSERBASE_API_KEY`: Your Browserbase API key
- `BROWSERBASE_PROJECT_ID`: The ID of the project you want to use for the tests

You can set these variables in a `.env` file in the root of this directory.

Then, run the tests with:

```sh
$ rye run test:e2e
```

## Writing tests

The tests are written using pytest and the [pytest-playwright](https://playwright.dev/python/docs/pytest) plugin.

You can find more information about writing tests in the [pytest documentation](https://docs.pytest.org/en/7.1.x/).

To submit a test, create a new file in the `e2e` directory with a name that describes the test and starts with `test_`.
