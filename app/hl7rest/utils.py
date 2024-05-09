

def get_dict_from_HL7(segment):
    """[summary]

    Arguments:
        segment {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    d = {}
    d['version'] = segment.version
    d['field'] = segment.name

    data = {}

    for s in segment.children:
        data[s.long_name] = s.value.replace('^', ' ')

    d['data'] = data

    return d


def value_or_default(req, key='', default=''):
    """[summary]

    Arguments:
        r {[type]} -- [description]

    Keyword Arguments:
        key {str} -- [description] (default: {''})
        default {str} -- [description] (default: {''})

    Returns:
        [type] -- [description]
    """
    try:
        return (req.GET[key] if req.method == 'GET' else req.POST[key])

    except Exception as e:
        print(e)

        return default
