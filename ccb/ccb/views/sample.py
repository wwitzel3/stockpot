from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from bson import ObjectId
import ccb.models as M

@view_config(route_name='sample', renderer='sample/index.mako')
def sample(request):
    return dict(samples=M.Sample.query.find())
    
@view_config(route_name='sample_instance', renderer='sample/instance.mako')
def sample_instance(request):
    sample_id = ObjectId(request.matchdict.get('id',None))
    sample = M.Sample.query.get(_id=sample_id)
    if not sample:
        raise HTTPNotFound
    return dict(sample=sample)
