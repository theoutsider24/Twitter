from invoke import task


@task
def coverage(c):
    c.run(
        "coverage run -m pytest && coverage run --append -m behave tests/service/features/ && coverage report && coverage xml"
    )


@task
def test(c):
    c.run("pytest && behave tests/service/features/")