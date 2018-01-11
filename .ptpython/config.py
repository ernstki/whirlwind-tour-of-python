# Source: https://github.com/jonathanslenders/ptpython/blob/master/examples/ptpython_config/config.py
def configure(repl):
    # Ask for confirmation on exit.
    repl.confirm_exit = False
    repl.show_status_bar = False
    repl.use_code_colorscheme('fruity')
