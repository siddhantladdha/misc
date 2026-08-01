alias p := pull

default:
  just --choose

pull:
  # Pull latest changes from the repository after stashing and pop stash after pull.
  git stash && git pull && git stash pop

squash:
  # To prevent size blowup.
  # Squash commits to the first commit.
  git reset --soft v0 && git commit --message="squooshed..." && git push --force
  git prune

## Notes
# Using `&&` to ensure that if the first command fails,
# the subsequent commands won't execute, preventing potential issues.
