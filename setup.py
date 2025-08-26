from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="CorreCLT",
    version="1.0",
    description="Projeto desenvolvido na disciplina de Programação Aplicada",
    executables=executables
)