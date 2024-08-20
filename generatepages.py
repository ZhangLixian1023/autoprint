import os
for i in range(1,45):
    os.system(f'xelatex -interaction=batchmode -jobname=p{i} "\def\param{{{i}}}\input{{template.tex}}"')