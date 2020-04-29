Title: Sign In With Apple
Tags: apple, auth
Category: Web Development
Date: 2020-04-05 20:24
Slug: sign-in-with-apple-you-should-know
comment_id: br549uekcydz-sign-in-with-apple-you-should-know
Subtitle: You Should Know
Summary: "Sign in with Apple" lets users log in to different apps and services using their Apple account. I document a few nuances and subtleties that I noticed in the course of integrating Apple authentication provider into a web app.
Keywords:

"Sign in with Apple" lets users log in to different apps and services using their Apple account. I document a few nuances and subtleties that I noticed in the course of integrating Apple authentication provider into a web app.

## Offering "Sign in with Apple" is obligatory

If your app lets a user sign in using any third-party service, then you must add Apple Login to the available options.

On September 12, 2019, Apple [introduced new guidelines for "Sign In With Apple"](https://developer.apple.com/news/?id=09122019b). It says, in the [fine print](https://developer.apple.com/app-store/review/guidelines/#sign-in-with-apple):

> Apps that use a third-party or social login service (such as Facebook Login, Google Sign-In, Sign in with Twitter, Sign In with LinkedIn, Login with Amazon, or WeChat Login) to set up or authenticate the user’s primary account with the app **must also offer Sign in with Apple as an equivalent option**.

Apple also announced the cutoff dates on which it will start enforcing this requirement.

> New apps must follow guideline 4.8 and Human Interface Guidelines on Sign in with Apple starting **April 30, 2020**. App updates must follow these guidelines starting **June 30, 2020**.

## Apple Developer Program membership is required

You must have an [Apple Developer Program account](https://developer.apple.com/support/compare-memberships/) to offer Apple login service in your app.

You need Apple developer console to create an App ID for your app. Similarly, you need to register a `client_id` and redirect URL for the app under the same App ID in the Apple developer console.

## You cannot use `localhost` for redirect URL

In the production, you will have a public redirect URL. During development and testing, we almost always use `localhost` or `127.0.0.1`. But Apple does not permit localhost URLs.

To quote the [documentation](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/configuring_your_webpage_for_sign_in_with_apple#3235722),

> The host specified in appleid-signin-redirect-uri must include a domain name. It can’t be an IP address or localhost.

An easy workaround is to map `localhost` to the registered redirect URL. You can do this by adding an entry to your [hosts file](<https://en.wikipedia.org/wiki/Hosts_(file)>).

For example, you set the redirect URL to `myapp.com/auth/apple/redirect` in the Apple developer console. Edit your `/etc/hosts` file and add this entry.

```
127.0.0.1    myapp.com
```

This mapping will let you develop and test Apple sign in locally, without touching your production server running at `myapp.com`.

**A couple of caveats**

You cannot use `.localhost` TLD, like `myapp.localhost`. It is because [`localhost` is reserved as a special-use domain](https://serverfault.com/a/882032/89869).

If you use `.dev` TLD like `myapp.dev`, then your dev server must support SSL. It is because browsers [force `.dev` domains to HTTPS](https://superuser.com/a/1251483/42415).

## Use "Sign in with Apple JS framework" to save time

Apple hosts a JavaScript script that does the heavy lifting for you.

<https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js>

You can use it:

1. to create and customize "Sign in with Apple" buttons,
1. to set authorization settings,
1. and to launch the authentication process.

The official documentation is available [here](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js).

## Use JS for ready-made branded button

Apple is very particular about how derivate work uses its brand. They have extensive Human Interface Guidelines on how to [display and offer Sign in With Apple button](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/overview/introduction/).

You can make your life easy, and use Apple JS Framework to create the button automatically.

```html
<div id="appleid-signin"></div>
<script
  type="text/javascript"
  src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"
></script>
```

The `appleid.auth.js` script will automatically replace the `appleid-signin` `div` with an SVG button. You can customize the button using `data-` attributes. Read more about it [here](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/displaying_sign_in_with_apple_buttons).

The **drawback** of this method is that the button will not become visible until the browser fetches, loads and runs the `appleid.auth.js` file. On slow networks and browsers, this will make for less than ideal user experience.

## Use Apple web service for ready-made branded button

The **better way** is to add branded "Sign in with Apple" button as an image to your assets. You can embed the image with base64 encoding to your HTML. Then the browser will paint the button as soon as it receives the HTML of the login page of your app.

Apple has set up a web service to generate a button for you.

<https://appleid.cdn-apple.com/appleid/button>

Simply send it GET request or open the link in your browser to download a PNG button. You can customize the button using query parameters. For instance, to download the button with a white background, and a border-radius of 5px, you would use the following URL.

[`https://appleid.cdn-apple.com/appleid/button?color=white&border_radius=5`](https://appleid.cdn-apple.com/appleid/button?color=white&border_radius=5)

You can read more about the available parameters [here](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/incorporating_sign_in_with_apple_into_other_platforms#3332112).

## Apple sends authorization result via HTTP POST

When you use `appleid.auth.js` framework, you have to [configure the authorization object](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/configuring_your_webpage_for_sign_in_with_apple#3235722) using `AppleID.auth.init()`. Then call `AppleID.auth.signIn()` when user clicks the sign-in button.

In the source code of `appleid.auth.js`, you will notice the `response_mode` is fixed to `form_post`. After Apple processes the authorization request, it sends the result using the HTTP POST method to the redirect URL you have set in the developer console. Therefore, your redirect URL should be a REST endpoint that can receive the POST and process it.

## Alternative to sign in with Apple JS framework

If you want to break away from the `appleid.auth.js` framework, you can send authorization request using HTTP GET method to this URL

<https://appleid.apple.com/auth/authorize>

Pass your `client_id` and other information using query parameters which are documented [here](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/incorporating_sign_in_with_apple_into_other_platforms#3332113).

Focus on query parameter `response_mode`. Its valid values are,

1. `query`
1. `fragment`
1. `form_post`

If you set the `response_mode` to `fragment` then, you do not need a REST API endpoint to receive the authorization result. Apple service will put the authorization result in the URL fragment. Hence, you can set redirect URL to a client-side HTML page. JavaScript code can pick the response from the URL fragment and process it.

!!! Caution

    Remember, the authorization result contains a JWT token, which is why I would **not** advise you to use `query` response mode.

    Unlike `query`, a URL fragment is not sent in HTTP request messages. It is not added to Referer header. The server does not receive the fragment. These benefits make `fragment` a more secure choice than a `query` to receive the result.

## Apple sends user information only once

You can set the [`scope`](https://developer.apple.com/documentation/sign_in_with_apple/clientconfigi/3230955-scope) to either name, or email, or both or neither. If you set the scope to name or email, Apple will send you a user object. The catch is, Apple sends user object only once.

To quote the [documentation](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/configuring_your_webpage_for_sign_in_with_apple#3331292),

> Apple only returns the user object the first time the user authorizes the app. Persist this information from your app; subsequent authorization requests won’t contain the user object.

Most apps will use the user information received from Apple. They will use it, for example, to send emails to the users, or to display the user’s name. Consequently, your app should store the user information for reuse.

Apple sends the user object again only if the user removes your app from the authorized apps from his Apple account and then tries to log in to your app again. You can leverage this tidbit to test the login multiple times during the development.

## Use `sub` claim for user identification

A user logs in using a third-party authentication provider, like Google. The user uses the email address "example@gmail.com" to log in to your app. User logs in to another instance of your app using Google. Your app will identify it is the same user because the email "example@gmail.com" matches in both cases.

It is a common scenario. [But it does not apply to Apple](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple#3384374).

[Apple lets your users protect their email address from your app.](https://support.apple.com/en-us/HT210425) When they sign in using Apple, Apple asks them if they want to hide their email address. If they do, then Apple sends a unique random email address in place of the actual email address. You can use this anonymous email address to communicate with your user, but you should not use it to identify the user.

Let's say, a user signs in to your app for the first time using Apple sign in. The user decides to conceal the email address. Apple creates a random email address for her, and sends it to your app, "random@privaterelay.appleid.com". The same user removes your app from authenticated apps in her Apple account, and signs in to your app again. This time the user decides to share the email address from you. Apple sends the email address "example@gmail.com". Now your app has two email addresses,

1. random@privaterelay.appleid.com
1. example@gmail.com

Both these email address belong to the same user, but your app cannot identify her if you only rely on email addresses to recognize the users.

You should use `sub` claim in JWT token for user identification. A `sub` claim is a unique identifier for the user, and it does not change when users hide or unhide their email addresses.

## `email_verified` claim is a string value

`email_verified` is one of the JWT claims. The [documentation](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple#3383773) says:

> **email_verified**<br />
> A Boolean value that indicates whether the service has verified the email.

But it is returned as a string, `"true"`, instead of a boolean value, `true`.

You can probably ignore it because the doc also mentions,

> The value of this claim is always true because the servers only return verified email addresses.

## Register your email domain

You can send emails to the Apple generated anonymous email addresses of the users. But to do that, you must [register your email domain](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/communicating_using_the_private_email_relay_service#3380020) in the Apple developer console.

Only registered email domains can send emails to the user. This feature eliminates spam emails for users who opt anonymous addresses.

## Helpful sites

**<https://jwt.io/>** is an outstanding tool to parse and validate tokens quickly.

You will [fetch Apple's public key](https://developer.apple.com/documentation/sign_in_with_apple/fetch_apple_s_public_key_for_verifying_token_signature) for verifying a token signature from [this link](https://appleid.apple.com/auth/keys). However, for unit testing, you might need to sign tokens using a custom generated key. **<https://mkjwk.org/>** is a simple JSON web key generator to generate random keys for testing.
