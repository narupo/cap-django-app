{@
    def usage():
        puts("Create Django application

Usage:

    $ cap make Capfile [project-name] [app-name] [options]

The options are:
    
    -h, --help             show usage
    -m, --models           model names (CSV format e.g Post,Article)
    -i, --install-label    The label of insert position in settings.py
")
        exit(0)
    end

    if opts.has("h") or opts.has("help"):
        usage()
    end

    p = opts.args(1)  // get project name
    n = opts.args(2)  // get app name
    if not (p and n):
        usage()
    end

    ms = opts.get("m") or opts.get("models") or "Sample"
    il = opts.get("i") or opts.get("install-label")

    // Copy directory
    puts("Copy template files...")
    exec("cap cp -r myapp :" + p + "/myapp")

    // Bake files
    puts("Bake template files...")
    exec("cap bake :" + p + "/myapp/models.py --models " + ms)
    exec("cap bake :" + p + "/myapp/admin.py --models " + ms)
    exec("cap bake :" + p + "/myapp/views.py --app-name " + n)

    // Install application (edit settings.py)
    if p and il:
        puts("Install application...")
        txt = "    '" + n + "',\n"
        exec("cap insert :" + p + "/" + p + "/settings.py \"" + txt + "\" --after " + il)
    end

    // Rename directory
    puts("Change directory name...")
    exec("cap mv :" + p + "/myapp/templates/myapp :" + p + "/myapp/templates/" + n)
    exec("cap mv :" + p + "/myapp :" + p + "/" + n)

    puts("Done")
@}
