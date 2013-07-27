@echo off
set /p comment="comments:"
git commit -am "%comment%"
git checkout gh-pages
git rebase master
git checkout master
git push