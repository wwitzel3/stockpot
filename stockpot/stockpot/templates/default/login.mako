<%inherit file="../base.mako"/>

		<div class="hero-unit">
			<h1>Login or Signup!</h1>
			<p>This site was created because we believe good friends and good food
			always pair well together. Our goal is to make it easy for you to create, organize,
			and share your favorite recipes with your friends, family, and communites. You can invite friends to add recipes or
			use recipes right from the site and once your cookbook is completed you can share with a select few or with everyone!
			You can even send it to print and have it delievered to your front door.</p>
		</div>
		<div class="row">
			<div class="span8">
				${signup_form|n}
			</div>
			<div class="span8">
				${login_form|n}
			</div>
		</div>
