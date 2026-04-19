from . import start, private, group, stats


def load_all(app):
    """Register all module handlers onto the Pyrogram app."""
    start.register(app)
    private.register(app)
    group.register(app)
    stats.register(app)


__all__ = ["load_all"]
