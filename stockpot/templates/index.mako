default index

%if logged_in:
<p>${logged_in}</p>
<p><a href="${request.route_url('logout')}">Logout</a></p>
%else:
<a href="${request.route_url('login')}">Login</a>
%endif
