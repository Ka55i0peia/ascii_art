from fastapi import FastAPI, Response
from pyfiglet import figlet_format

app = FastAPI()


@app.get("/asciinize")
def asciinize(
    text: str = "hi there!",
    font: str = "univers",
    width: str = 200,
):
    """Returns ascii version of text.

    :param text: input text, defaults to "hi there!"
    :param font: font of the ascii art. Check out http://www.figlet.org/examples.html for
        samples, defaults to "univers"
    :param width: length of the ascii art, defaults to 200
    :return: raw text of ascii art
    """
    ascii_art = figlet_format(text, font, width=width)
    return Response(content=ascii_art, media_type="text/plain")


if __name__ == "__main__":
    asciinize()
