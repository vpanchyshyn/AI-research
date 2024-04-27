def create_acronym(sent: str) -> str:
    """
    >>> create_acronym("random access memory\\nAs soon As possible")
    'RAM - random access memory\\nASAP - As soon As possible'
    """
    if not sent:
        return None
    if isinstance(sent, str):
        sent_ = sent.split('\n')
        acr=''
        one_fraze = ''
        ful = ''
        for fraze in sent_:
            sent_1=fraze.split()
            for words in sent_1:
                prt_acr=words[:1]
                acr+=prt_acr.upper()
            one_fraze += acr +' - ' + fraze
            ful+=one_fraze + '\n'
            one_fraze = ''
            acr = ''
        for t in ful:
            if 48<=ord(t)<=57:
                return None
        return ful.rstrip('\n')
    return None
