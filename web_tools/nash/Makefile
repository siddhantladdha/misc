SHELL = bash
.ONESHELL:

all: nash.html index.html

clean:
	@rm *.html

nash.html:
	@m4 <<- 'EOF' > $@
		changequote({{{,}}})dnl
		define(_NASH_TITLE, Nash : Note as HTML)dnl
		define(_NASH_FILE_NAME, {{{}}})dnl
		define(_NASH_BODY, <p></p>)dnl
		include(src/nash.m4)
	EOF

index.html:
	@m4 <<- 'EOF' > $@
		changequote({{{,}}})dnl
		define(_NASH_TITLE, {{{👋 Hello, This is Nash}}})dnl
		define(_NASH_FILE_NAME, {{{👋 Hello, This is Nash}}})dnl
		define(_NASH_BODY, {{{include(src/hello.html)}}})dnl
		include(src/nash.m4)
	EOF
