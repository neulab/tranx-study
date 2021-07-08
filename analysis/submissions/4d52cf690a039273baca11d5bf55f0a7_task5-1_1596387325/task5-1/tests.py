import re

from main import EMAIL_REGEX

def test_email_regex():
    assert re.match(EMAIL_REGEX, "foo@bar.com")
    assert not re.match(EMAIL_REGEX, "aaa")
    assert not re.match(EMAIL_REGEX, "aaa.bbb")
