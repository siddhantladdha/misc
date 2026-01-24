# A hacky makefile without any concern for portability.
# Why a hacky workaround? Coz I would rather work on circuits then 
# [piece of shit makefiles](https://stackoverflow.com/questions/961942/what-is-the-worst-programming-language-you-ever-worked-with/962719#962719).
report: report.md
	pandoc --from=markdown --output=report.pdf --filter=pandoc-citeproc --bibliography=citations.bib --csl=ieee.csl --pdf-engine=xelatex --pdf-engine-opt=shell-escape report.md

