def view_root(context, request):
    return {'items':list(context), 'project':'stockpot'}

def view_model(context, request):
    return {'item':context, 'project':'stockpot'}
