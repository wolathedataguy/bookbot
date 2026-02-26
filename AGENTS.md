## Cursor Cloud specific instructions

BookBot is a zero-dependency Python 3 CLI tool. No package manager or virtual environment is needed.

### Running the application

```
python3 main.py <path_to_book>
```

The `books/` directory is `.gitignore`'d. Before running, ensure a text file exists there (e.g., download Frankenstein from Project Gutenberg):

```
mkdir -p books
curl -sL https://www.gutenberg.org/cache/epub/84/pg84.txt -o books/frankenstein.txt
python3 main.py books/frankenstein.txt
```

### Testing

There is no test suite or linter configured in this project. Validate changes by running the CLI against a sample book file and checking stdout output.
