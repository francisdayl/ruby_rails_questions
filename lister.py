import pyperclip

listado_str = "\n".join([f'\n### {i}. ' for i in range(190,250)])

print(listado_str)


pyperclip.copy(listado_str)
