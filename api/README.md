# Overview
All commands should be run from `ai-lms/api/`.

# Operation
## Dependencies
To add a new dependency, add a `python_requirement()` target to `dep/BUILD`.

## Lockfile
This is a prerequisite for many of the other steps. It should be run every time you add
a new dependency to `dep/BUILD`:
```
pants generate-lockfiles
```

## Running
### Local
Generate the lockfile, then do:
```
pants run src/main.py
```

### Deployment
The API is deployed as a private service on Render. It will use the lockfile that is
committed to the repo. If you want to simulate what happens in Render, do:
```
pants package src:binary
./dist/src/binary.pex
```

## Local environment
This creates a local environment for your IDE or for raw (non-`pants`) commands.
Of course, you can still run `pants` commands in this environment if you want.
Generate the lockfile, then do:
```
pants export --py-resolve-format=symlinked_immutable_virtualenv --resolve=default
```

To activate, do:
```
source dist/export/python/virtualenvs/default/3.13.7/bin/activate
```

Then, do `which python` to see the executable path. Point your IDE to that.