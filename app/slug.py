from app.extensions import db

from sqlalchemy.orm import declarative_mixin
from sqlalchemy.event import listens_for

from slugify import slugify

@declarative_mixin
class HasSlug:
    slug_target_column = "title"
    slug = db.Column(db.String, unique=True, nullable=False)

@listens_for(db.session, "before_commit")
def update_slugs(session):
    new_items = [item for item in session.new if isinstance(item, HasSlug)]
    dirty_items = [item for item in session.dirty if isinstance(item, HasSlug)]
    all_items = new_items + dirty_items

    if not all_items:
        return
    
    slugs_map = {}
    for item in all_items:
        table = item.__table__

        if table not in slugs_map:
            slugs_map[table] = set(
                c[0] for c in session.execute(db.select(table.c.slug))
            )

        item_slug = item.slug or ""
        title = getattr(item, item.slug_target_column)
        slug = slugify(title)

        if item_slug.startswith(slug):
            continue

        i = 1

        while slug in slugs_map[table]:
            slug = slugify(title) + "-" + str(i)
            i += 1

        item.slug = slug
        slugs_map[table].add(slug)