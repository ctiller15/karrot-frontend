ids_uri_pattern_delim = ','

# must correspond to the regex found in yunity_swagger.py
def _named_regex(name, regex):
    return '(?P<{name}>{regex})'.format(name=name, regex=regex)


def _create_integerid(minlength, maxlength):
    integerid = '[0-9]{{{minlength},{maxlength}}}'.format(minlength=minlength, maxlength=maxlength)
    return integerid


def multiple_integerids(name, minlength=1, maxlength=10, minrepetitions=1, maxrepetitions=200, delim=ids_uri_pattern_delim):
    """
    :type name: str
    :type minlength: int
    :type maxlength: int
    :type minrepetitions: int
    :type maxrepetitions: int
    :rtype str
    """
    return _named_regex(
        name=name,
        regex='{integerid}({delim}{integerid}){{{minrepetitions},{maxrepetitions}}}'.format(
            integerid=_create_integerid(minlength, maxlength),
            minrepetitions=minrepetitions - 1,
            maxrepetitions=maxrepetitions - 1,
            delim=delim,
        ),
    )


def single_integerid(name, minlength=1, maxlength=10):
    return _named_regex(name=name, regex=_create_integerid(minlength, maxlength))


chat_id_uri_pattern = single_integerid('chat')
user_id_uri_pattern = single_integerid('user')
multiple_user_id_uri_pattern = multiple_integerids('users')

item_id_uri_pattern = single_integerid('item')

group_id_uri_pattern = single_integerid('group')