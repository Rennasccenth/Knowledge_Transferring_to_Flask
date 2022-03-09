import os
from src.app.kenzie.system import mk_database


def initialize():
    # [to com sono já, são 4:12AM] Pra que é exatamente isso aqui?
    # Não é melhor verificar se o arquivo json (./src/app/database/database.json) ja foi criado?
    #
    # if not os.path.isdir("./src/app/database"):
    if not os.path.isdir(os.environ.get("DATABASE_PATH")):
        mk_database()


if __name__ == '__main__':
    initialize()
