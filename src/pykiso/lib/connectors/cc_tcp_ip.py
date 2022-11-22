##########################################################################
# Copyright (c) 2010-2022 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
Communication Channel via socket
********************************

:module: cc_socket

:synopsis: connector for communication via socket

.. currentmodule:: cc_socket

"""
import logging
import socket
from typing import Dict, Union

from pykiso import CChannel

log = logging.getLogger(__name__)


class CCTcpip(CChannel):
    """Connector channel used to communicate via socket"""

    def __init__(self, dest_ip: str, dest_port: int, max_msg_size: int = 256, **kwargs):
        """Initialize channel settings.

        :param dest_ip: destination ip address
        :param dest_port: destination port
        :param max_msg_size: the maximum amount of data to be received
            at once
        """
        super().__init__(**kwargs)
        self.dest_ip = dest_ip
        self.dest_port = int(dest_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_msg_size = max_msg_size
        # Set a timeout to send the signal to the GIL to change thread.
        # In case of a multi-threading system, all tasks will be called one after the other.
        self.timeout = 1e-6

    def _cc_open(self) -> None:
        """Connect to socket with configured port and IP address."""
        log.info(
            f"Connection to socket at address {self.dest_ip} port {self.dest_port}"
        )
        self.socket.settimeout(3)
        self.socket.connect((self.dest_ip, self.dest_port))

    def _cc_close(self) -> None:
        """Close UDP socket."""
        log.info(
            f"Disconnect from socket at address {self.dest_ip}, port {self.dest_port}"
        )
        self.socket.close()

    def _cc_send(self, msg: bytes or str, raw: bool = False) -> None:
        """Send a message via socket.

        :param msg: message to send
        :param raw: is the message in a raw format (True) or is it a string (False)?
        """
        if msg is not None and raw is False:
            msg = msg.encode()

        log.debug(f"Sending {msg} via socket to {self.dest_ip}")
        self.socket.send(msg)

    def _cc_receive(
        self, timeout=0.01, raw: bool = False
    ) -> Dict[str, Union[bytes, str, None]]:
        """Read message from socket.

        :param timeout: time in second to wait for reading a message
        :param raw: should the message be returned raw or should it be interpreted as a
            pykiso.Message?

        :return: Message if successful, otherwise none
        """
        self.socket.settimeout(timeout or self.timeout)

        try:
            msg_received = self.socket.recv(self.max_msg_size)

            if not raw:
                msg_received = msg_received.decode().strip()

            log.debug(f"Socket at {self.dest_ip} received: {msg_received}")
        except socket.timeout:
            log.exception(
                f"encountered timeout error while receiving message via {self}"
            )
            return {"msg": None}
        except Exception:
            log.exception(f"encountered error while receiving message via {self}")
            return {"msg": None}

        return {"msg": msg_received}
