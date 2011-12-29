<form name='login' action='${request.route_url('login')}' class='form-stacked' method='post'>
<fieldset>
<legend>Already have an account?</legend>
<div class="clearfix">
<label for="xlInput">Login or Email</label>
<div class="input">
<input class="xlarge" name="login" size="30" type="text">
</div>
</div>

<div class="clearfix">
<label for="xlInput">Password</label>
<div class="input">
<input class="xlarge" name="password" size="30" type="text">
</div>
</div>

<div class="actions">
<button name="form.login" type="submit" class="btn primary">Log In</button>
</div>
</fieldset>
</form>
