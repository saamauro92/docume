watch_sass: sass
	watchmedo shell-command --patterns="*.scss" --recursive --command 'make sass' static/scss

sass:
	sassc static/scss/style.scss --sourcemap