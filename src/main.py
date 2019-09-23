from config.config import Config
from handler.handler import Handler
from server.server import Server


CONFIG_FILE_NAME = 'httpd.conf'


def main():
    config = Config()
    config.read(CONFIG_FILE_NAME)

    handler = Handler(config.document_root)

    server = Server(config, handler)
    server.launch()


if __name__ == '__main__':
    main()
