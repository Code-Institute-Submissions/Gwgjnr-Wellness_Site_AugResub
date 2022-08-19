from django.contrib.sitemaps import Sitemap
from virtual_sessions.models import Session


class ArticleSitemap(Sitemap):
    '''
    Dynamic Sitemap Class
    '''
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Session.objects.all()

    def lastmod(self, obj):
        '''
        Dynamic Sitemap Class
        '''
        return obj.article_published

    def location(self, obj):
        '''
        Set Sitemap location
        '''
        return '/seminars/%s' % (obj.article_slug)
