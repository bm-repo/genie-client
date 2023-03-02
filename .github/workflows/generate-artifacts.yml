on:
  pull_request:
    branches:
      - main
      - develop

jobs:
  artifacts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - run: mkdir -p path/to/artifact

      - run: echo hello1 > path/to/artifact/test_file1.txt
      - run: echo hello2 > path/to/artifact/test_file2.txt

      - name: Tar files
        run: tar -cvf testcases.tar path/to/artifact

      - uses: actions/upload-artifact@v3
        with:
          name: testcases-artifact
          path: testcases.tar
