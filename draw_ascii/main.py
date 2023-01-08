from fastapi import FastAPI, Response
from pyfiglet import figlet_format

app = FastAPI()


@app.get("/asciinize")
def asciinize(
    text: str = "hi there!",
    font: str = "univers",
    width: str = 200,
):
    ascii_art = figlet_format(text, font, width=width)
    return Response(content=ascii_art, media_type="text/plain")


if __name__ == "__main__":
    asciinize()
