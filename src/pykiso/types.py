##########################################################################
# Copyright (c) 2010-2022 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
Define some recurring typing definitions
"""

import pathlib
import typing

from . import message

PathType = typing.Union[str, pathlib.Path]
MsgType = typing.Union[message.Message, bytes, str]
