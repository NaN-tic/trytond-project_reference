# This file is part project_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .work import *

def register():
    Pool.register(
        Work,
        module='project_reference', type_='model')
