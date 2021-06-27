{@
	def usage():
		puts("Usage: cap make admin.py [options]

The options are:

	-m, --models   model names (CSV format, e.g Post,Article)
")
		exit(0)
	end

	if opts.has("h") or opts.has("help"):
		usage()
	end

	ms = opts.get("m") or opts.get("models")
	names = []
	if ms:
		names = ms.split(",")
	end
@}from django.contrib import admin
{@
	for i = 0; i < len(names); i += 1:
		n = names[i]
		N = n.capitalize()
@}from .models import {: N :}
{@
	end
@}

{@
	for i = 0; i < len(names); i += 1:
		n = names[i]
		N = n.capitalize()
@}class {: N :}Admin(admin.ModelAdmin):
    fields = ['TODO']
    list_display = ['TODO']
    search_fields = ['TODO']
    list_filter = ['created', 'modified']

admin.site.register({: N :}, {: N :}Admin)


{@
	end
@}

