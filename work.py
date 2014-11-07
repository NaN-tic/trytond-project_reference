# This file is part project_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Work']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'
    reference = fields.Reference('Reference', selection='get_reference',
        select=True)

    @classmethod
    def _get_reference(cls):
        'Return list of Model names for Reference'
        return []

    @classmethod
    def get_reference(cls):
        IrModel = Pool().get('ir.model')
        models = cls._get_reference()
        models = IrModel.search([
                ('model', 'in', models),
                ])
        return [(None, '')] + [(m.model, m.name) for m in models]
