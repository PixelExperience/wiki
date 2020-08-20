FROM shreejoy/pex-wiki:latest

COPY . /app

CMD ["bash", "run.sh"]
