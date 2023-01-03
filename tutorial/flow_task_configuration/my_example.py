#!/usr/bin/env python

from prefect import flow, task

@task(name="My Example Task",
      description="And example task for a tutorial.",
      tags=["tutorial","tag-test"])

def my_task():
    # do some work
    pass

@flow(name="My Example Flow"
      description="An example flow for a tutorial",
      version="tutorial_02")
def my_flow():
    my_task()
