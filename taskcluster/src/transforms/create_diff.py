from taskgraph.transforms.base import TransformSequence
import os

transforms = TransformSequence()

@transforms.add
def add_comment_scopes(config, tasks):
    pr_number = str(os.environ.get("GITHUB_PULL_REQUEST_NUMBER", -1))
    project = config.params['project'].lower()
    for task in tasks:
        scopes = task.setdefault("scopes", [])
        scopes.append(f"ap:apdiff:action:diff:{pr_number}")
        scopes.append(f"ap:apdiff:repo:{project}")
        yield task
