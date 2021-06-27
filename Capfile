{@
	def usage():
		puts("Create Django application

Usage:

	$ cap make Capfile [app-name] [options]

The options are:
	
	-h, --help             show usage
	-m, --models           model names (CSV format e.g Post,Article)
	-p, --project-name     Django project name
	-i, --install-label    The label of insert position in settings.py
")
		exit(0)
	end

	if opts.has("h") or opts.has("help"):
		usage()
	end

	n = opts.args(1)  // get app name
	if n == nil:
		usage()
	end

	ms = opts.get("m") or opts.get("models")
	p = opts.get("p") or opts.get("project-name")
	il = opts.get("i") or opts.get("install-label")

	// Copy directory
	puts("Copy template files...")
	exec("cap cp -r myapp :myapp")

	// Bake files
	puts("Bake...")
	exec("cap bake :myapp/models.py --models " + ms)
	exec("cap bake :myapp/admin.py --models " + ms)
	exec("cap bake :myapp/views.py --app-name " + n)


	// Install application (edit settings.py)
	puts("Install application...")
	if p and il:
		txt = "    '" + n + "',\n"
		exec("cap insert :" + p + "/settings.py \"" + txt + "\" --after " + il)
	end

	// Rename directory
	puts("Change directory name...")
	exec("cap mv :myapp/templates/myapp :myapp/templates/" + n)
	exec("cap mv :myapp :" + n)

	puts("Done")
@}
