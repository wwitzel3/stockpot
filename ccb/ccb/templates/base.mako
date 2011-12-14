<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>Community Cookbook</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />

  <link rel="stylesheet/less" href="${request.static_url('ccb:static/lib/bootstrap.less')}">
  <link rel="shortcut icon" href="${request.static_url('ccb:static/favicon.ico')}" />
  <link rel="stylesheet/less" href="${request.static_url('ccb:static/style.less')}" media="screen" charset="utf-8" />


  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  <script src="${request.static_url('ccb:static/less-1.1.5.min.js')}"></script>
  <script type="text/javascript" src="${request.static_url('ccb:static/script.js')}"></script>

</head>
<body>
	<div class="topbar">
		<div class="fill">
			<div class="container">
				<a class="brand" href="#">Cookbook</a>
				<ul class="nav">
					<li class="active"><a href="#">Home</a></li>
					<li><a href="#about">About</a></li>
					<li><a href="#signup">Signup</a></li>
				</ul>
			</div>
		</div>
	</div>

	<div class="container">
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
				<h2>Signup</h2>
				<p>Signing up is easy, use your existing Google, Twitter, or Facebook account.</p>
				<p><a class="btn" href="${request.route_url('signup')}">Signup</a></p>
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

<p>user_id: ${user_id}</p>

 			</div>
		</div>
	</div>
</body>
</html>
