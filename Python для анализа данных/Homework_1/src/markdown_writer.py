import os

class Markdown_writer():
    def __init__(self, path: str) -> None:
        """
        Generate class for write in Markdown file

        Args:
            file (str): path to the file
        """
        if os.path.exists(path): 
            os.remove(path)
        self.path = path
        self.double_command = {
            'italic': '*',
            'bold': '**',
            'italic_bold': '***'
        }
        self.single_command = {
            'header': '#',
            'slide': '---'
        }
    
    def write(self, text: str) -> None:
        """
        Function for write in file

        Args:
            text (str): text to write
        """
        with open(self.path, 'a+', encoding='utf-8') as f:
            f.write(text)
        
    def write_in_file(self, text: str = None, command: str = None) -> None:
        """
        Write text in file with command attribute
        List of commands:
        1) 'italic';
        2) 'bold';
        3) 'italic_bold';
        4) 'header';
        5) 'slide';

        Args:
            text (str): text to write in file. Defaults to None.
            command (str, optional): addictional command for writing. Defaults to None.
        """
        if command in self.double_command.keys():
            self.write(self.double_command[command]+text+self.double_command[command]+'  '+'\n')
        elif command in self.single_command.keys():
            self.write(self.single_command[command]+' '+text+'  '+'\n')
        elif command is None:
            self.write(text+'  '+'\n')
        elif command is None and text is None:
            raise ValueError('Не указан ни один из атрибутов, ничего не будет изменено')
        else:
            raise Exception('Непредвиденное поведение функции, стоит проверить код')