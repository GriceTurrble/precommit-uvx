# python-project-template

Pre-commit action to run a uvx command

## Archived

This was an interesting experiment, but I don't think it's particulary useful.
I may reference this for use in better hooks later, though.

## Usage

In `.pre-commit-config.yaml`, use the following as an example:

```yaml
- repo: https://github.com/griceturrble/precommit-uvx
  rev: "main"
  always_run: true
  hooks:
    - id: uvx
      types_or:
        - pyi
        - python
      args: [flake8]
```

The hook simply calls `uvx` with the give `args` on any file match the `type_or` array.

Pre-commit passes a list of files to this command after any `args` are given.
If `always_run` is set to `true`, it runs on all files in the repo every time,
not simply the files that are staged for a commit.

Thus, the above example will run `flake8` to lint all python files in the repo when hooks are called.

## Why?

It was a fun experiment in making a pre-commit hook.
If it turns out there is a need for running a tool not already enabled in pre-commit
but that can easily be run by calling that tool with `uvx`,
then this hook provides a kind of command runner for arbitrary Python tools.
