<form name='signup' action='${request.route_url('login')}' class='form-stacked' method='post'>
<fieldset>
<legend>Create your free account.</legend>
<div class="clearfix">
<label for="xlInput">Username</label>
<div class="input">
<input class="xlarge" name="username" size="30" type="text">
</div>
</div>

<div class="clearfix">
<label for="xlInput">Email Address</label>
<div class="input">
<input class="xlarge" name="email" size="30" type="text">
<span class="help-block">We promise we won't share your email with anyone.</span>
</div>
</div>

<div class="clearfix">
<label for="xlInput">Password</label>
<div class="input">
<input class="xlarge" name="password" size="30" type="text">
</div>
</div>

<div class="clearfix">
<label for="xlInput">Confim Password</label>
<div class="input">
<input class="xlarge" name="password_verify" size="30" type="text">
</div>
</div>

<div class="actions">
<button type="submit" name="form.signup" class="btn primary">Create an account</button>
</div>
</fieldset>
</form>

<br/>

			<form name="facebook" action="/velruse/facebook/auth" method="post">
			<input type="hidden" name="end_point" value="http://communitycookbook.net:6543/login" />
			<input type="hidden" name="scope" value="publish_stream,create_event" />
			</form>

			<form name="twitter" action="/velruse/twitter/auth" method="post">
			<input type="hidden" name="end_point" value="http://communitycookbook.net:6543/login" />
			</form>

<a class="fb-button" href="javascript:document.facebook.submit();">&nbsp;</a>
<br/>
<a class="twitter-button" href="javascript:document.twitter.submit();">&nbsp;</a>
