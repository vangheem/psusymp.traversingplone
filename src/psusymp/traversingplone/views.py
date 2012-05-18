from zope.interface import implements
from Products.Five import BrowserView
from psusymp.traversingplone.interfaces import ITestUtil


class TestUtil(BrowserView):
    implements(ITestUtil)

    def foobar(self):
        return 'hello world'


class TestView(BrowserView):

    def foobar_util(self):
        context = self.context
        request = self.request
        from zope.component import getMultiAdapter
        util = getMultiAdapter((context, request), name='test-util')
        return util.foobar()
