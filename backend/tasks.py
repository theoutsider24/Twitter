from invoke import task


@task
def coverage(c):
    c.run("coverage run -m pytest && coverage report && coverage xml")


@task
def test(c):
    c.run("pytest")


@task
def pylint(c):
    c.run("pylint twitter/ tests/")


@task
def lint(c):
    print("---Black---")
    c.run("black . --check")
    print("---Pylint---")
    c.run("pylint twitter/ tests/")
    print("---Isort---")
    c.run("isort . --check-only")
    print("---Mypy---")
    c.run("mypy .")
