from textwrap import dedent           
from west.commands import WestCommand 
from west import log           

class Tool(WestCommand):

    def __init__(self):
        '''
        `self.name`: 命令名字，将被存储在 `self.name` 属性中
        `self.help`: 单行帮助信息，简要描述命令的用途。在 west --help 时显示
        `self.description`: 多行描述，详细说明命令的用途和使用方式。在 west mycommand --help 时显示
        '''
        super().__init__(
            'realtek-bee',
            'Realtek tools for west framework',
            dedent('''
            Realtek tools for west framework'''))

    def do_add_parser(self, parser_adder):
        '''
        `do_add_parser(self, parser_adder)` 方法用于添加命令行解析器。
        可以完全自定义命令行参数解析行为。
        `parser_adder` 是一个subparser，是 `argparse.ArgumentParser.add_subparsers()` 的返回值
        '''
        parser = parser_adder.add_parser(self.name,
                                         help=self.help,
                                         description=self.description)

        parser.add_argument('-t', '--tool', required=True, help='rtk tool name')
        return parser

    def do_run(self, args, unknown_args):
        log.inf('--optional is', args.tool)

