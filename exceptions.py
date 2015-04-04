class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class CmdFailure(Error):
    """Exception raised for a forked command failing.

    Attributes:
        cmd -- cmd that was being run
        msg  -- explanation of the error
    """

    def __init__(self, cmd, msg):
        self.cmd = cmd
        self.msg = msg


class TestAssertionFailure(Error):
    """Exception raised when a test assertion failed.

    Attributes:
        test -- test that was being asserted
        msg  -- explanation of the error
    """

    def __init__(self, test, msg):
        self.test = test
        self.msg = msg