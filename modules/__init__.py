from . import start, private, group, stats

def load_all(app):
    start.register(app)
    private.register(app)
    group.register(app)
    stats.register(app)

__all__ = ["load_all"]
