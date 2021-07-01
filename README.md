# Cap's template project for Django

This project is template project for Django application by Cap.

# Usage

First, Clone this project to your file system.
And set Cap's home directory to this project.

```
$ # Clone template project
$ git clone https://github.com/narupo/cap-django-app
$
$ # And set Cap's home
$ cap home cap-django-app
$ cap ls
```

Next, Create Django project and move to that project directory.

```
$ # Create Django project
$ django-admin startproject mysite
```

And Execute `Capfile` for build.

```
$ # Build application
$ cap build mysite blogapp --models Article,Comment
$ ls
```
