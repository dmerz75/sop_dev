#!/bin/sh

# USE:
# ./render_equation.sh zeta

pdflatex current.tex
pdfcrop current.pdf
# pdftoppm current-crop.pdf|pnmtopng > equation_$1.png
# convert current-crop.pdf equation_$1.svg
# convert current-crop.pdf equation_$1.eps
convert current-crop.pdf equation_$1_small.png
cp current-crop.pdf equation_$1.pdf
cp current.tex equation_$1.tex
