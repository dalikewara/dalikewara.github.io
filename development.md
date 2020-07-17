# Development

### Activating virtual env

```bash
source venv/bin/activate
```

### Listening Pelican

```bash
pelican --listen --autoreload
```

### Listening SASS

```bash
sass --no-source-map --watch themes/rujak-cingur/sass/master.scss:themes/rujak-cingur/static/css/master.min.css --style compressed
```