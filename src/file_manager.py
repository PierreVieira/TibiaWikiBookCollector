from abc import ABC


class FileManager:
    __metaclass__ = ABC

    @staticmethod
    def get_url() -> str:
        with open('../text_files/url.txt') as arq:
            content_file = arq.read()
        if content_file is None or content_file == '':
            raise ValueError('O conteúdo do arquivo "url.txt" não pode estar vazio')
        return content_file

    @staticmethod
    def set_output(books: "list[str]") -> None:
        string = '\n'.join(books)
        with open('../text_files/output.txt', 'w', encoding='utf8') as arq:
            arq.write(string)
