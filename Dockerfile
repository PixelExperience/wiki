FROM pixelexperience/wiki_ci:latest

COPY . /app

CMD ["bash", "run.sh"]
