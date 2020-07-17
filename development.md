# Development

### Activate virtual env

```bash
source venv/bin/activate
```

### Listen Pelican

```bash
pelican --listen --autoreload
```

### Listen SASS

```bash
sass --no-source-map --watch themes/rujak-cingur/sass/master.scss:themes/rujak-cingur/static/css/master.min.css --style compressed
```