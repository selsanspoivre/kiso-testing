##########################################################################
# Copyright (c) 2010-2022 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
:module: exceptions

:synopsis: Define all custom exceptions raised by pykiso framework

.. currentmodule:: exceptions
"""


class PykisoError(Exception):
    """Pykiso specific exception used as basis for all others."""

    def __str__(self):
        return self.message


class AuxiliaryCreationError(PykisoError):
    """Raised when an auxiliary instance creation failed."""

    def __init__(self, aux_name: str) -> None:
        """Initialize attributes.

        :param aux_name: aux alias
        """
        self.message = f"Auxiliary {aux_name} failed at instance creation"
        super().__init__(self.message)
