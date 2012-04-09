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

<ul>
%for error in errors:
<li>${error}</li>
%endfor
</ul>

${form('facebook', 'Login with Facebook',
       scope='email,publish_stream,read_stream,create_event,offline_access')}

<form id="register" action="${request.route_url('login')}" method="post">
  <input type="text" name="email" value="" />
  <input type="text" name="username" value="" />
  <input type="password" name="password" value="" />
  <input type="submit" name="form.submitted" value="Register" />
</form>

<form id="login" action="${request.route_url('login')}" method="post">
  <input type="text" name="email" />
  <input type="password" name="password" />
  <input type="submit" name="form.auth" value="Login" />
</form>

</body>
</html>
