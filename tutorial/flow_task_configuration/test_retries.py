from prefect import flow, task

# this task runs 3 times before the flow fails
@task(retries=2, retry_delay_seconds=6)
def failure():
    print('running')
    raise ValueError("bad code")

@flow
def test_retries():
    return failure()

test_retries()
