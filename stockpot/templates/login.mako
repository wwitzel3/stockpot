<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Auth Page</title>
</head>
<body>

<%def name="form(name, title, **kw)">
<form id="${name}" action="${login_url(request, name)}" method="post">
    % for k, v in kw.items():
    <input type="hidden" name="${k}" value="${v}" />
    % endfor
    <input type="submit" value="${title}" />
</form>
</%def>

${form('facebook', 'Login with Facebook',
       scope='email,publish_stream,read_stream,create_event,offline_access')}

</body>
</html>
