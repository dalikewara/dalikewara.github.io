# Development

### Set up virtualenv

```bash
virtualenv venv
```

### Activate virtualenv

```bash
source venv/bin/activate
```

### Install requirements

Activate virtualenv, then;

```bash
pip3 install -r requirements.txt
```

### Listen Pelican

```bash
pelican --listen --autoreload
```

### Listen SASS

```bash
sass --no-source-map --watch themes/rujak-cingur/sass/master.scss:themes/rujak-cingur/static/css/master.min.css --style compressed
```