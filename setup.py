import sys
from cx_Freeze import setup, Executable
build_exe_options={"packages":["PyPDF2","tkinter","reportlab","random","PIL","os","pyqrcode","sqlite3"],"include_files":["cnt1","cnt2","fundo1.png","logo.png"]}
setup(
    name = "Credenciais",
    version = "1",
    options = {"build_exe":build_exe_options},
    executables = [Executable("cred.py")])
