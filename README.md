# ROULETTE - API

This API has all logic about simple bets with a Casino Roulette

## Installation

To install this project run

```bash
  docker compose up --build roulette-api
```

The next step, open the shell from Docker Container **roulette-api**

```bash
λ docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                    NAMES       
0713bfcb3a67   roulette-api   "python run.py"          17 seconds ago       Up 14 seconds       0.0.0.0:8000->8000/tcp   roulette-api
5bcbb83aeabd   postgres:12    "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:6543->5432/tcp   roudb
```

With the **Container ID** of **roulette-api** image run

```bash
  docker exec -it <CONTAINER ID> bash
```

Into the Container bash run 

```bash
  root@<CONTAINER ID>:/app# flask db init
```

```bash
  root@<CONTAINER ID>:/app# flask db migrate -m "Initial migration."
```

```bash
  root@<CONTAINER ID>:/app# flask db upgrade
```

With this you can have all model about **Roulette - API**
