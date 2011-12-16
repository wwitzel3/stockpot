<%inherit file="../base.mako"/>

<form id="user.profile" method="POST" action="">
<div class="clearfix">
            <label for="username">Username</label>
            <div class="input">
              <input class="xlarge" id="username" name="username" size="30" type="text" value="${request.user.username}" />
            </div>
          </div>
<div class="actions">
            <input type="submit" class="btn primary" value="Save changes">&nbsp;<button type="reset" class="btn">Cancel</button>
          </div>
</form>

<ul>
	<li>Provider: ${request.user.provider}</li>
	<li>Identifier: ${request.user.identifier}</li>
</ul>
