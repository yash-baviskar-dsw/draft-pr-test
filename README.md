# Draft PR CI demo

A tiny Python project for trying a GitHub pull request workflow. The workflow runs
pytest, Pylint, and Bandit when a PR targeting `main` is marked **Ready for review**.
It also runs on pushes to `main`. Updates to a draft PR are intentionally skipped.

## Run locally

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m pylint main.py test_main.py
python -m bandit -r main.py
```

`main.py` contains a small `greet` function and `test_main.py` checks its output.
Change the function or add code on your feature branch to see the checks pass or fail.

## Try the PR flow

1. Commit and push these starter files to `main`.
2. Create a feature branch from `main`, make a change, and push it.
3. Open a **draft** pull request targeting `main`. CI is skipped while it is draft.
4. Click **Ready for review**. The workflow runs all three checks.
5. Push further changes to the ready PR; the checks run again.

## Require passing checks before merge

After the first workflow run has reported its check name to GitHub:

1. Open the repository's **Settings → Rules → Rulesets** (or **Branches** on older
   repository settings pages) and create a rule/ruleset targeting `main`.
2. Require a pull request before merging and require the status check named
   **`checks`** (job in the **Python CI** workflow) to pass.
3. Save the rule. Confirm the PR's merge box says the required check is pending or
   passed; GitHub will block merging when it fails.

The workflow file alone runs the checks; this GitHub setting makes the result a
merge requirement. GitHub requires the workflow to have reported the check at least
once before it can be selected in some branch protection screens.
