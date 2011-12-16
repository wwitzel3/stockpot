<%inherit file="../base.mako"/>

		<div class="hero-unit">
			<h1>Community Cookbook</h1>
			<p>This site was created because we believe good friends and good food
			always pair well together. Our goal is to make it easy for you to create, organize,
			and share your favorite recipes with your friends, family, and communites. You can invite friends to add recipes or
			use recipes right from the site and once your cookbook is completed you can share with a select few or with everyone!
			You can even send it to print and have it delievered to your front door.</p>
		</div>
		<div class="row">
			<div class="span-one-third">
				<h2>Features</h2>
				<ul>
					<li>Easily share recipes</li>
					<li>Invite friends to add recipes</li>
					<li>Organize recipes in to different books</li>
					<li>Private and public recipes</li>
				</ul>
			</div>
			<div class="span-one-third">
				<h2>Coming Soon</h2>
				<ul>
					<li>Recipe suggestions</li>
					<li>On-Demand Printing</li>
				</ul>
			</div>
			<div class="span-one-third">
			%if userid:
				<h2>Get Started!</h2>
				<ul>
					<li><a href="${request.route_url('user.profile', userid=userid)}">Update profile</a></li>
					<li>Create a cookbook</li>
					<li>Add recipes</li>
					<li>Invite friends</li>
				</ul>
			%else:
				<h2>Signup</h2>
				<p>Signing up is easy, use your existing Google, Twitter, or Facebook account.</p>
			<form action="/velruse/google/auth" method="post">
				<input type="hidden" name="popup_mode" value="popup" />
				<input type="hidden" name="end_point" value="http://communitycookbook.net:6543/login" />
				<input type="submit" value="Login with Google" />
			</form>

			<form action="/velruse/facebook/auth" method="post">
			<input type="hidden" name="end_point" value="http://communitycookbook.net:6543/login" />
			<input type="hidden" name="scope" value="publish_stream,create_event" />
			<input type="submit" value="Login with Facebook" />
			</form>

			<form action="/velruse/twitter/auth" method="post">
			<input type="hidden" name="end_point" value="http://communitycookbook.net:6543/login" />
			<input type="submit" value="Login with Twitter" />
			</form>
			
			%endif

 			</div>
		</div>
