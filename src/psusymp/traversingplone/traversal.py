from zExceptions import NotFound
from zope.publisher.interfaces.browser import IBrowserPublisher
from OFS.SimpleItem import SimpleItem
from zope.interface import implements
from content import CustomContent


class CustomTraverseContext(SimpleItem):
    implements(IBrowserPublisher)

    def __init__(self, context, request):
        super(CustomTraverseContext, self).__init__(context, request)
        self.id = 'custom-traversal'
        self.Title = lambda: u'Custom Area'
        self.context = context

    def publishTraverse(self, request, name):
        try:
            return self.context[name].__of__(self)
        except KeyError:
            item = CustomContent(self.context, request, name)
            return item.__of__(self)

    def browserDefault(self, request):
        return self, ('@@view',)

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)


from psusymp.traversingdjango.models import Person
from django.core.exceptions import ObjectDoesNotExist
from content import DjangoContent


class CustomDjangoTraverseContext(SimpleItem):
    implements(IBrowserPublisher)

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

    def browserDefault(self, request):
        raise NotFound

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)
