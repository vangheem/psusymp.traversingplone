from zope.publisher.interfaces.browser import IBrowserPublisher
from OFS.SimpleItem import SimpleItem
from zope.interface import implements


class CustomContent(SimpleItem):
    implements(IBrowserPublisher)

    def __init__(self, context, request, id):
        super(CustomContent, self).__init__(context, request)
        self.id = id
        self.Title = lambda: id
        self.context = context

    def browserDefault(self, request):
        return self, ('@@view',)

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)


class DjangoContent(SimpleItem):
    implements(IBrowserPublisher)

    def __init__(self, context, request, obj):
        super(DjangoContent, self).__init__(context, request)
        self.id = str(obj.id)
        self.Title = lambda: obj.name
        self.obj = obj
        self.context = context

    def browserDefault(self, request):
        return self, ('@@view',)

    def getPhysicalPath(self):
        return self.context.getPhysicalPath() + (self.id,)
