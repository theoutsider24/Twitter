# Build Log

## 2023-08-26

Initialised repo! 🎉

Some issues with dev containers, wanted to treat this as a monorepo with a dev container for
each package but VSCode doesn't support being able to do that while also having access to git
so I've gone with a single dev container.

Starting on the backend, used Poetry (because it's the best) to get started, installed FastAPI
but haven't started APIs yet. Trying out Behave instead of pytest-bdd which is my go-to. It's
interesting, the context is similar to what I've done in the past but fixtures are quite different.

Haven't decided on a database yet so using an in-memory repository for now.

Mostly following my usual pattern of splitting domain and service with an API layer to come later.

I'm trying out `invoke` to help with the more complec test running required by the Behave
test-runner. I'm also having a terrible time trying to get the dev container to pick up on file
events, seems to be an issue with Docker Desktop in windows with WSL2. I'm going to try checking
out the repo directly into a WSL2 distro and running from there, it's suggested that may work
better.
