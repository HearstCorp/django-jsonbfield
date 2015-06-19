**Note: This is basically a standalone version of the JSONB support in the Postgres contrib package of the Django master branch, targeted for the Django 1.9 release.** 

JSONField
---------

.. versionadded:: 1.9

.. class:: JSONField(**options)

    A field for storing JSON encoded data. In Python the data is represented in
    its Python native format: dictionaries, lists, strings, numbers, booleans
    and ``None``.

.. note::

    PostgreSQL has two native JSON based data types: ``json`` and ``jsonb``.
    The main difference between them is how they are stored and how they can be
    queried. PostgreSQL's ``json`` field is stored as the original string
    representation of the JSON and must be decoded on the fly when queried
    based on keys. The ``jsonb`` field is stored based on the actual structure
    of the JSON which allows indexing. The trade-off is a small additional cost
    on writing to the ``jsonb`` field. ``JSONField`` uses ``jsonb``.

    **As a result, the usage of this field is only supported on PostgreSQL
    versions at least 9.4**.

Querying JSONField
^^^^^^^^^^^^^^^^^^^^

We will use the following example model::

    from django.contrib.postgres.fields import JSONField
    from django.db import models

    class Dog(models.Model):
        name = models.CharField(max_length=200)
        data = JSONField()

        def __str__(self):  # __unicode__ on Python 2
            return self.name

.. fieldlookup:: jsonfield.key

Key, index, and path lookups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To query based on a given dictionary key, simply use that key as the lookup
name::

    >>> Dog.objects.create(name='Rufus', data={
    ...     'breed': 'labrador',
    ...     'owner': {
    ...         'name': 'Bob',
    ...         'other_pets': [{
    ...             'name': 'Fishy',
    ...         }],
    ...     },
    ... })
    >>> Dog.objects.create(name='Meg', data={'breed': 'collie'})

    >>> Dog.objects.filter(data__breed='collie')
    [<Dog: Meg>]

Multiple keys can be chained together to form a path lookup::

    >>> Dog.objects.filter(data__owner__name='Bob')
    [<Dog: Rufus>]

If the key is an integer, it will be interpreted as an index lookup in an
array::

    >>> Dog.objects.filter(data__owner__other_pets__0__name='Fishy')
    [<Dog: Rufus>]

If the key you wish to query by clashes with the name of another lookup, use
the :lookup:`jsonfield.contains` lookup instead.

If only one key or index is used, the SQL operator ``->`` is used. If multiple
operators are used then the ``#>`` operator is used.

.. warning::

    Since any string could be a key in a json object, any lookup other than
    those listed below will be interpreted as a key lookup. No errors are
    raised. Be extra careful for typing mistakes, and always check your queries
    work as you intend.

Containment and key operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fieldlookup:: jsonfield.contains
.. fieldlookup:: jsonfield.contained_by
.. fieldlookup:: jsonfield.has_key
.. fieldlookup:: jsonfield.has_any_keys
.. fieldlookup:: jsonfield.has_keys

:class:`~django.contrib.postgres.fields.JSONField` shares lookups relating to
containment and keys with :class:`~django.contrib.postgres.fields.HStoreField`.

- :lookup:`contains <hstorefield.contains>` (accepts any JSON rather than
  just a dictionary of strings)
- :lookup:`contained_by <hstorefield.contained_by>` (accepts any JSON
  rather than just a dictionary of strings)
- :lookup:`has_key <hstorefield.has_key>`
- :lookup:`has_any_keys <hstorefield.has_any_keys>`
- :lookup:`has_keys <hstorefield.has_keys>`
