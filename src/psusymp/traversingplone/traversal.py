from zExceptions import NotFound
from OFS.SimpleItem import SimpleItem

from zope.interface import implements
from zope.component import adapts
from zope.location.interfaces import LocationError
from zope.publisher.interfaces import IPublishTraverse
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest

from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

from django.core.exceptions import ObjectDoesNotExist
from psusymp.traversingdjango.models import Person

from psusymp.traversingplone.content import CustomContent
from psusymp.traversingplone.content import DjangoContent


class CustomTraverseContext(SimpleItem):
    implements(IPublishTraverse)

    allowed_ids = ['foobar', 'testing', 'hello']

    def __init__(self, context, request):
        super(CustomTraverseContext, self).__init__(context, request)
        self.id = 'custom-traversal'
        self.Title = lambda: u'Custom Area'
        self.context = context

    def publishTraverse(self, request, name):
        if name in self.allowed_ids:
            item = CustomContent(self.context, request, name)
            return item.__of__(self)
        raise NotFound

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)


class CustomDjangoTraverseContext(SimpleItem):
    implements(IPublishTraverse)

    def __init__(self, context, request):
        super(CustomDjangoTraverseContext, self).__init__(context, request)
        self.id = 'django-traversal'
        self.Title = lambda: u'Django Area'
        self.context = context

    def publishTraverse(self, request, id):
        try:
            obj = Person.objects.get(id=id)
            return DjangoContent(self.context, request, obj).__of__(self)
        except ObjectDoesNotExist:
            raise NotFound

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)


class PlusPlusTraversal(object):
    implements(ITraversable)
    adapts(IPloneSiteRoot, IHTTPRequest)

    allowed_ids = ['foobar', 'testing', 'hello']

    def __init__(self, context, request=None):
        self.context = context
        self.request = request

    def traverse(self, name, ignore):
        if name in self.allowed_ids:
            return CustomContent(self.context, self.request, name)
        raise LocationError


class PlusPlusDjangoTraversal(object):
    implements(ITraversable)
    adapts(IPloneSiteRoot, IHTTPRequest)

    allowed_ids = ['foobar', 'testing', 'hello']

    def __init__(self, context, request=None):
        self.context = context
        self.request = request

    def traverse(self, name, ignore):
        try:
            obj = Person.objects.get(id=name)
            return DjangoContent(self.context, self.request, obj)
        except ObjectDoesNotExist:
            raise LocationError
