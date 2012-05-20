from collective.routes import addRoute
from psusymp.traversingdjango.models import Person
from django.core.exceptions import ObjectDoesNotExist
from psusymp.traversingplone.content import CustomContent
from psusymp.traversingplone.content import DjangoContent


def customFinder(context, **kwargs):
    query = context.query
    if 'name' in query and query['name'] in ['foobar', 'testing', 'hello']:
        return CustomContent(context, context.request, query['name'])

addRoute('Custom Content', '/customcontent/{name}',
         objectFinder=customFinder)


def customDjangoFinder(context, **kwargs):
    query = context.query
    if 'name' in query:
        try:
            obj = Person.objects.get(id=query['name'])
            return DjangoContent(context, context.request, obj)
        except ObjectDoesNotExist:
            return

addRoute('Django Content', '/djangocontent/{name}',
         objectFinder=customDjangoFinder)
