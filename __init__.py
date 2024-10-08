import re
from aqt import gui_hooks

def replace_review_count(html:str, klass: str) -> str:
    ''' Find any span with the given class that has non-zero numeric data, replace data with ?'''
    pattern = re.compile(r'<span class=["]*' + re.escape(klass) + r'["]*>[1-9]+[0-9]*</span>')
    return re.sub(pattern, f'<span class="{klass}">?</span>', html)

def update_home_review_counts(browser, content) -> None:
    content.tree = replace_review_count(content.tree, klass='new-count')
    content.tree = replace_review_count(content.tree, klass='learn-count')
    content.tree = replace_review_count(content.tree, klass='review-count')

def update_overview_review_counts(overview, content) -> None:
    content.table = replace_review_count(content.table, klass='new-count')
    content.table = replace_review_count(content.table, klass='learn-count')
    content.table = replace_review_count(content.table, klass='review-count')

gui_hooks.deck_browser_will_render_content.append(update_home_review_counts)
gui_hooks.overview_will_render_content.append(update_overview_review_counts)
