# mygraph/schema.py
"""Чтобы создать типы GraphQL для каждой из наших моделей Django, подкласс класса DjangoObjectType
автоматически определит поля GraphQL, соответствующие полям в моделях Django.
После того, как мы это сделали, мы перечислим эти типы как поля в классе Query.
"""

import graphene
from graphene_django import DjangoObjectType

from mygraph.models import Category, Book


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "books")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "name", "notes", "category")


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_books(root, info):
        # We can easily optimize query count in the resolve method
        return Book.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
