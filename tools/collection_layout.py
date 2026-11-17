#!/usr/bin/env python3
"""Repository layout rule for the generated collection.

The numbered chapters (00_MASTER_INDEX.md ... 25_FINAL_ARCHITECTURE_ASSESSMENT.md)
live in chapters/, not at the collection root. The generators in this directory
emit root-relative paths, so every markdown write goes through route(), which

  * sends a root-level chapter file to chapters/<name>;
  * rebuilds the relative links inside that file so they still resolve from the
    new location (chapter-to-chapter links stay bare, links into other
    directories gain the ../ prefix).

Files that are already in a subdirectory, and non-markdown writes, are returned
untouched unless they are themselves chapter files.
"""
import posixpath
import re

CHAPTER = re.compile(r'^[0-9]{2}_[A-Z0-9_]+\.md$')
LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
SCHEME = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*:')


def new_path(rel):
    """Collection-relative path of `rel` once chapters live in chapters/."""
    return 'chapters/' + rel if CHAPTER.match(rel) else rel


def rebase_links(text, old_rel, new_rel):
    """Return `text` with its relative markdown links valid from `new_rel`."""
    def fix(match):
        target = match.group(2).strip()
        if SCHEME.match(target) or target.startswith('#'):
            return match.group(0)
        base, sep, anchor = target.partition('#')
        base = base.strip().rstrip('/')
        if not base:
            return match.group(0)
        old_abs = posixpath.normpath(posixpath.join(posixpath.dirname(old_rel), base))
        if old_abs.startswith('..'):
            return match.group(0)
        link = posixpath.relpath(new_path(old_abs), posixpath.dirname(new_rel) or '.')
        if target.endswith('/'):
            link += '/'
        if sep:
            link += '#' + anchor
        return match.group(0) if link == target else '[' + match.group(1) + '](' + link + ')' 

    return LINK.sub(fix, text)


def route(rel, text):
    """Return (collection-relative output path, text) for one generated file."""
    if not rel.endswith('.md'):
        return rel, text
    new_rel = new_path(rel)
    return new_rel, rebase_links(text, rel, new_rel)
