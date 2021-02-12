# -*- coding: utf-8 -*- #
"""
Twitter Meta
============

This plugin adds Twitter meta tags to articles.

Use like this in your base.html template:

.. code-block:: jinja2

  {% if article and article.twittermetatags %}
  {% for tag in article.twittermetatags.names %}
  <meta name="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% for tag in article.twittermetatags.properties %}
  <meta property="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% endif %}

  {% if page and page.twittermetatags %}
  {% for tag in page.twittermetatags.names %}
  <meta name="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% for tag in page.twittermetatags.properties %}
  <meta property="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% endif %}

"""
import os.path
from urllib.parse import urljoin, urlparse

from pelican import generators, signals
from pelican.utils import strftime
from bs4 import BeautifulSoup


def twitter_meta_tag_articles(content_generators):

    for generator in content_generators:
        if isinstance(generator, generators.ArticlesGenerator):
            for article in (
                    generator.articles +
                    generator.translations +
                    generator.drafts):
                twitter_meta_tag(article)
        elif isinstance(generator, generators.PagesGenerator):
            for page in generator.pages:
                twitter_meta_tag(page)

    return True


def twitter_meta_tag(item):
    tag_names = [('twitter:card', 'summary_large_image')]
    tag_properties = []

    # title
    tag_names.append(('twitter:title', item.title))

    # Description
    default_summary = item.summary
    description = item.metadata.get('twitter_description', default_summary)
    tag_names.append(('twitter:description', description))

    # Image
    image = item.metadata.get('twitter_image', '')
    if not image:
        soup = BeautifulSoup(item._content, 'html.parser')
        img_links = soup.find_all('img')
        if  (len(img_links) > 0):
            image = img_links[0].get('src')
            if image.startswith("{filename}"):
                image = image[11:]
            if not "http" in image:
                if item.settings.get('SITEURL', ''):
                    image = urljoin(item.settings.get('SITEURL', ''), image)
    if image:
        tag_names.append(('twitter:image', image))

    # site
    site = item.settings.get('TWITTER_META_SITE', None)
    if site:
        tag_names.append(('twitter:site', site))

    # creator
    creator = item.metadata.get('twitter_creator', site)
    if creator:
        tag_names.append(('twitter:creator', creator))

    # domain
    domain = urlparse(item.settings.get('SITEURL', '')).netloc
    tag_properties.append(('twitter:domain', domain))

    # url
    url = os.path.join(item.settings.get('SITEURL', ''), item.url)
    tag_properties.append(('twitter:url', url))

    item.twittermetatags = {
      "names": tag_names,
      "properties": tag_properties,
    }

    # default_locale = item.settings.get('LOCALE', [])
    # if default_locale:
    #     default_locale = default_locale[0]
    # else:
    #     default_locale = ''
    # ogtags.append(
    #     ('og:locale', item.metadata.get('og_locale', default_locale)))

    # ogtags.append(('og:site_name', item.settings.get('SITENAME', '')))

    # ogtags.append(('article:published_time',
    #                strftime(item.date, "%Y-%m-%d")))

    # if hasattr(item, 'modified'):
    #     ogtags.append(('article:modified_time', strftime(
    #         item.modified, "%Y-%m-%d")))

    # if hasattr(item, 'related_posts'):
    #     for related_post in item.related_posts:
    #         url = os.path.join(item.settings.get('SITEURL', ''), related_post.url)
    #         ogtags.append(('og:see_also', url))

    # author_fb_profiles = item.settings.get('AUTHOR_FB_ID', {})
    # if len(author_fb_profiles) > 0:
    #     for author in item.authors:
    #         if author.name in author_fb_profiles:
    #             ogtags.append(
    #                 ('article:author', author_fb_profiles[author.name]))

    # ogtags.append(('article:section', item.category.name))

    # try:
    #     for tag in item.tags:
    #         ogtags.append(('article:tag', tag.name))
    # except AttributeError:
    #     pass


def register():
    signals.all_generators_finalized.connect(twitter_meta_tag_articles)
