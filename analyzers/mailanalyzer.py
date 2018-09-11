# -*- coding: utf-8 -*-
from analyzers import RegexAnalyzer


class MailAnalyzer(RegexAnalyzer):
    """Analyzer to match on email addresses via regex"""
    name = "MailAnalyzer"

    def __init__(self, action):
        # Regex taken from http://emailregex.com/
        regex = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
        super().__init__(action, regex)
