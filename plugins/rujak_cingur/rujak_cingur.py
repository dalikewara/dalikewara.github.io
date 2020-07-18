from pelican import signals

def test(sender):
    print('test')

def register():
    signals.initialized.connect(test)