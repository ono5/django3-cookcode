from django.http import HttpResponseBadRequest


# from common.decorators import ajax_required

def ajax_required(f):
    '''
    ajaxリクエストのみを許可するデコレータ
    以下のようにして使用する
    @ajax_required
    def test():
        pass
    '''
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            # raise 400 error
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

