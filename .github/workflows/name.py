name: LEGENDX

on: push

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v2

      - name: Find and Replace

        uses: jacobtomlinson/gha-find-replace@master

        with:

          find: "LEGENDX22"

          replace: "LEGENDBOT"

      - name: Create Pull Request

        uses: stefanzweifel/git-auto-commit-action@v4

        with:

          commit_message: 'Replaced new name'

          commit_options: '--no-verify'

          repository: .

          commit_user_name: LEGENDXOP

          commit_user_email: legendxx08377@gmail.com
