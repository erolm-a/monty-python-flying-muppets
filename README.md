# Monty Python Flying Muppet: An exploration of S-BERT for the people who "didn't like the movie""

## Description

The home edition DVD release of the famous "Monty Python's Holy Grail" was famous to contain a subtitle track for "the people who don't like the movie", containing somewhat related sentences extracted from Shakespeare's Henry IV script. The effect was quite hilarious and I wondered what it could be like if I used a pre-trained language model (e.g. S-BERT) to achieve this.

## Setup

Create a virtual environment and then install all the dependencies in the requirements file.

```bash
python -m venv venv

# On Linux
source venv/bin/activate

# On Windows
venv/bin/activate.bat

git clone https://github.com/erolm-a/monty-python-flying-muppet
cd monty-python-flying-muppet
pip install -r requirements
```

Then you need to find yourself a corpus of Henry IV script in txt format (or anything you like) and a transcript of the Holy Grail (or anything else you want). Then use the script as self-documented, and Tom's your uncle.

## License

WTFPL
