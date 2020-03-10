#!/bin/sh
# Credit: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_data_files() {
  git checkout master
  git add -f data/*.csv
  git commit -m "Automatic Travis update" -m "[skip ci]"
}

upload_files() {
  # Remove existing "origin"
  git remote rm origin
  # Add new "origin" with access token in the git URL for authentication
  git remote add origin https://${GITHUB_API_KEY}@github.com/leoncvlt/covid-19-uk-data.git > /dev/null 2>&1
  git push origin master --quiet
}

setup_git
commit_data_files
upload_files