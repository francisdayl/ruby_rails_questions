import pyperclip

listado_str = "\n".join([f'\n### {i}. ' for i in range(1,150)])

print(listado_str)


pyperclip.copy(listado_str)
