Title: Create Apple And Google Sign-In Buttons
Subtitle: Quick And Dirty Way
Tags: imagemagick, firefox, hack, branding
Category: Web Development
Date: 2020-03-19 19:32
Slug: create-apple-and-google-signin-buttons
comment_id: qgv9kzow41p8-create-apple-and-google-signin-buttons
Summary:
Keywords:

Both Apple and Google have extensive guidelines on how to use their respective logos and create sign-in buttons that use their services.

1. [Google Sign-In Branding Guidelines](https://developers.google.com/identity/branding-guidelines)
1. [Apple Sign-In Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/overview/buttons/)

Both companies provide their logo artwork for download, in both vector and raster formats, that you can use to create these buttons.

1. [Google Sign-In Assets](https://developers.google.com/identity/branding-guidelines)
1. [Apple Design Resources](https://developer.apple.com/design/resources/)

## Apple sign-in button example

Apple has a helpful article [Displaying Sign in with Apple Buttons](https://developer.apple.com/documentation/signinwithapplejs/displaying_sign_in_with_apple_buttons) on their website. It has a sample HTML code that if you write to a file and open the file in the browser, it will show you their branded sign-in button.

```html
<html>
  <head>
    <meta name="appleid-signin-client-id" content="[CLIENT_ID]" />
    <meta name="appleid-signin-scope" content="[SCOPES]" />
    <meta name="appleid-signin-redirect-uri" content="[REDIRECT_URI]" />
    <meta name="appleid-signin-state" content="[STATE]" />
  </head>
  <style>
    .signin-button {
      width: 210px;
      height: 40px;
    }
  </style>
  <body>
    <div
      id="appleid-signin"
      class="signin-button"
      data-color="black"
      data-border="true"
      data-type="sign in"
    ></div>
    <script
      type="text/javascript"
      src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"
    ></script>
  </body>
</html>
```

The `appleid.auth.js` script replaces the `div` that has the id `appleid-signin` with their SVG files.

## Google sign-in button example

If you visit the Google documentation on [Building a custom Google Sign-In button](https://developers.google.com/identity/sign-in/web/build-button), it has a ready to use sign-in button example, which complies with their guidelines.

## The quick and dirty way to create sign-in buttons

If I were working on a serious project, I would have used their SVG logos and
created reusable button components using React. Though, it will be arduous to ensure
the buttons match their policies. I am sure a designer worth their salt would not see it as a challenge. But I am no designer.

I needed "Sign in with Google" and "Sign in with Apple" buttons for a **temporary** project. So I decided to phone it in.

I would customize the size and some minor attributes of the example buttons on their website using the browser's "Inspector" tool and then take screenshots of them. I will use those images in my project.

I could have used the scripts they provide to load the buttons from their servers, but my project was going to run in an offline environment.

The button size I require is 210x50 with no rounded corners.

### Makeshift Google sign-in button

I opened the Google documentation that has the [example
button](https://developers.google.com/identity/sign-in/web/build-button) in the
Firefox Developer Edition browser. Why Firefox Developer Edition? I will get to that, but it is essential to have Firefox Developer Edition.

I right-clicked and examined the button. It is almost the same size that I require.

<div class="elegant-gallery" itemscope itemtype="http://schema.org/ImageGallery">
  <figure
    itemprop="associatedMedia"
    itemscope
    itemtype="http://schema.org/ImageObject"
  >
    <a
      href="/images/create-apple-google-signin-buttons-quick-dirty-way-edit-google.png"
      itemprop="contentUrl"
      data-size="2282x806"
    >
      <img
        src="/images/create-apple-google-signin-buttons-quick-dirty-way-edit-google-thumbnail.png"
        itemprop="thumbnail"
        alt="Inspect and edit the HTML of the Google sign-in button"
      />
    </a>
    <figcaption itemprop="caption description">
      Inspect and edit the HTML of the Google sign-in button
    </figcaption>
  </figure>
</div>

I only had to

1. Disable `box-shadow` in CSS
1. Set `border-radius` to 0
1. Set the width to 210px from 240px

Luckily, the width change is only minor; otherwise, the button and logo would get out of proportion.

I right-clicked the node and chose "Screenshot Node" option. This feature is why I used Firefox Developer Edition. It is one of the many features that make Firefox Developer Edition more effective than Chrome for web developers.

<div class="elegant-gallery" itemscope itemtype="http://schema.org/ImageGallery">
  <figure
    itemprop="associatedMedia"
    itemscope
    itemtype="http://schema.org/ImageObject"
  >
    <a
      href="/images/create-apple-google-signin-buttons-quick-dirty-way-screenshot-node.png"
      itemprop="contentUrl"
      data-size="1042x744"
    >
      <img
        src="/images/create-apple-google-signin-buttons-quick-dirty-way-screenshot-node-thumbnail.png"
        itemprop="thumbnail"
        alt="Screenshot Node option in Firefox Developer"
      />
    </a>
    <figcaption itemprop="caption description">
      Screenshot Node option in Firefox Developer
    </figcaption>
  </figure>
</div>

### Makeshift Apple sign-in button

Apple sign-in button required a little extra work because they do not have any HTML button on their documentation site. Their documentation uses images of buttons to explain their guidelines.

No big deal. Remember the HTML code I [mentioned earlier](#apple-sign-in-button-example)? I modified it a little so that the button has a white background. You can see and run the code yourself [here](https://repl.it/@talha131/Displaying-Sign-in-with-Apple-Buttons).

![Sign in with Apple Default Button](/images/create-apple-google-signin-buttons-quick-dirty-way-default-apple.png)

This button has rounded corners. On examining the rendered HTML in the browser inspector, I noticed it uses SVG for the border.

Removing `ry` attribute from the SVG removed the rounded corners.

```svg
<rect width="100%" height="100%" ry="15%" fill="#fff" stroke="black" stroke-width="1" stroke-linecap="round"></rect>
```

I adjusted the height of the root `div` from 40px to 50px. Width was already 210px. Then I right clicked on the root `div` and selected the "Screenshot Node" option.

![Sign in with Apple button has white border](/images/create-apple-google-signin-buttons-quick-dirty-way-apple-white-border.png)

The resulting image had white borders outside the black outline of the button. I am not sure what the reason is.

It's a quick and dirty hack. So I didn't investigate it further. Instead, I set the `background-color` of the `body` to black using Firefox's CSS editor.

Now when I took the screenshot of the node, the result did not have the white border.

![Sign in with Apple button with black border](/images/create-apple-google-signin-buttons-quick-dirty-way-apple-black-border.png)

### Adjust the image size

Now I examined the image sizes using the good, old, trusty [ImageMagick](https://imagemagick.org/).

```bash
$ identify apple.png
apple.png PNG 1260x300 1260x300+0+0 8-bit sRGB 22512B 0.000u 0:00.000
$ identify google.png
google.png PNG 420x100 420x100+0+0 8-bit sRGB 5914B 0.000u 0:00.000
```

Focus on the part that comes after `PNG`. That's the dimension.

You see that `google.png` dimension is 420x100. But in the browser, I set it to
210x50. What happened? Retina display happened. My machine has a retina display
because of which this image is 2x its set size.

Apple button size is enormous. I have to cut it down.

```bash
convert apple.png -resize x100 apple-h100.png
```

`-resize` tells ImageMagick to resize the input image.

`x100` means set the height to 100, and adjust the width to keep the perspective.

Let's check the dimensions of the result.

```bash
$ identify apple-h100.png
apple-h100.png PNG 420x100 420x100+0+0 8-bit Gray 256c 4725B 0.000u 0:00.000
```

So now I have a Google sign-in button image, and an Apple sign-in button image, in my required dimensions, which 100% conforms to the official guidelines.

I ran both the images through [ImageOptim](https://imageoptim.com/mac) to reduce their sizes, which decreased their sizes to 4kb each.

![Sign in with Google](/images/create-apple-google-signin-buttons-quick-dirty-way-google.png)

![Sign in with Apple](/images/create-apple-google-signin-buttons-quick-dirty-way-apple.png)

## Conclusion

Honestly, it took me more time to write this article than it took me to get the image buttons.

But should you use this _"technique"_ in the production?

Although each image
has a minuscule size of 4kb each, your web page will still have to make
additional two requests to the server to fetch them. Usually, we want to
minimize the number of requests to the server to improve the page's
performance. Therefore, I would not advise using it in production.

Then again, it is possible to use loader like [this](https://www.npmjs.com/package/base64-inline-loader) to convert your image to base64 encoded strings automatically and inline them. If your build pipeline supports such loader, then you can use the images without worrying about the additional requests. But if you use the loader for too many images, then your page size will get hefty.

So choose wisely!
