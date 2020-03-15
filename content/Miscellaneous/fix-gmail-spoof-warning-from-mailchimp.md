Title: Fix Gmail Spoof Warning From Mailchimp
Tags: newsletter, email, domain, email-forwarding
Category: Miscellaneous
Date: 2020-03-15 14:31
Slug: fix-gmail-spoof-warning-from-mailchimp
comment_id: umelpz3xqscd-fix-gmail-spoof-warning-from-mailchimp
Subtitle:
Summary: Using Gmail to send a Mailchimp newsletter to your subscriber can cause a spoof message warning. It looks unprofessional and may drive out your subscribes. I detail a solution to this problem in this article.
Keywords:

I set up Mailchimp to send latest release notification to [Pelican - Elegant theme](https://elegant.oncrashreboot.com/){: class="ampl"} users. Setting up the newsletter was easy, thanks to the Mailchimp's easy to follow UI and beginner-friendly walkthroughs.

When the first newsletter went out, I received the email too. To my surprise, Gmail placed a banner on top of the email.

<div class="elegant-gallery" itemscope itemtype="http://schema.org/ImageGallery">
<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<a
      href="/images/gmail-spoof-warning-mailchimp.png"
      itemprop="contentUrl"
      data-size="2754x334"
    >
      <img
        src="/images/gmail-spoof-warning-mailchimp-thumbnail.png"
        itemprop="thumbnail"
        alt="Gmail Spoof Warning"
      />
    </a>
    <figcaption itemprop="caption description">
      Gmail Spoof Warning
    </figcaption>
  </figure>
</div>

It reads,

> **Be careful with this message**

> This may be a spoofed message. The message claims to have been sent from your account, but Gmail couldn't verify the actual source. Avoid clicking links or replying with sensitive information, unless you are sure you actually sent this message. (No need to reset your password, the real sender does not actually have access to your account!)

After a little digging, I discovered that Mailchimp recommends [verifying your email domain](https://mailchimp.com/help/verify-a-domain/). But I use Gmail, which I cannot verify as my email domain. These free email providers have [certain limitations](https://mailchimp.com/help/limitations-of-free-email-addresses/), which in turns, causes the spoof warning.

Luckily I own the domain [`onCrashReboot`](https://www.oncrashreboot.com/). I use [Netlify](https://www.netlify.com/) to do DNS management for my domain.

What I need is to set up email forwarding on `oncrashreboot.com` domain to my Gmail address, or set up an email hosting service on the domain. Then create an email address like `elegant@oncrashreboot.com`. Then I need to verify the new email address with Mailchimp.

[Zoho Mail](https://www.zoho.com/mail/) offers a free plan for email hosting. But using it would mean I have to check Zoho mail for emails that I receive on the `elegant@oncrashreboot.com` address, besides my primary email address. Or [setup email forwarding from Zoho to Gmail](https://www.zoho.com/mail/help/email-forwarding.html), and [configure Zoho mail to send emails from Gmail account](https://help.zoho.com/portal/en/community/topic/sending-mails-from-gmail-as-alias). It seemed like to much work, also I am not sure how reliable this setup would be.

There is another service [ImprovMX](https://improvmx.com/) that specializes in setting up email forwarding, quickly and painlessly. It has a guide to [setup free email forwarding with Netlify](https://improvmx.com/guides/netlify/).

!!!Tip Recommendation

    After using ImprovMX, I must say it is one of the simplest and easiest web services to use. Kudos to their team. I highly recommend them.

## Configure your DNS to use ImprovMX

Log into DNS management service, in my case, Netlify, and following records.

| Record Type | Name | Priority | Value                                  |
| ----------- | ---- | -------- | -------------------------------------- |
| MX          | @    | 10       | `mx1.improvmx.com`                     |
| MX          | @    | 20       | `mx2.improvmx.com`                     |
| TXT         | @    |          | `v=spf1 include:spf.improvmx.com ~all` |

## Create ImprovMX account

Got to [ImprovMX](https://improvmx.com/), and enter your domain name and email address, in my case, my Gmail address.

Next login to [ImprovMX](https://app.improvmx.com/login), and click on "Prefer to connect using your domain's DNS entry?". Provide your domain and the email address.

<div class="elegant-gallery" itemscope itemtype="http://schema.org/ImageGallery">
<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<a
      href="/images/gmail-spoof-warning-improvmx-register.png"
      itemprop="contentUrl"
      data-size="1760x266"
    >
      <img
        src="/images/gmail-spoof-warning-improvmx-register-thumbnail.png"
        itemprop="thumbnail"
        alt="ImprovMX Account Registration Form"
      />
    </a>
    <figcaption itemprop="caption description">
      ImprovMX Account Registration Form
    </figcaption>
  </figure>
</div>

## Create your email alias

Login to ImprovMX dashboard after your account verification. Make sure email forwarding is active.

Create an email alias for your domain like `elegant@oncrashreboot.com`.

## Verify domain in Mailchimp

Login to your Mailchimp account and go to Account → Settings → Domains.

<div class="elegant-gallery" itemscope itemtype="http://schema.org/ImageGallery">
<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<a
      href="/images/gmail-spoof-warning-mailchimp-verify-domain.png"
      itemprop="contentUrl"
      data-size="1224x538"
    >
      <img
        src="/images/gmail-spoof-warning-mailchimp-verify-domain-thumbnail.png"
        itemprop="thumbnail"
        alt="Verify Domain Button"
      />
    </a>
    <figcaption itemprop="caption description">
      Verify Domain Button
    </figcaption>
  </figure>
</div>
Click on "Verify Domain" button. Enter the email address alias you created in ImprovMX, in my case `elegant@oncrashreboot.com`.

Mailchimp will send a verification code to your email alias, which then ImprovMX will forward to your email account.

Enter the verification code in the Mailchimp form and complete the process.

## Update your Mailchimp campaigns

Got to your campaigns and click "Pause & Edit Campaign" on one of your campaigns. Go to "Setup" step, and edit "From email address" field.

Set to the alias you just verified.

Save and exit the form. Reactivate your campaign.

Repeat this process for all your campaigns, that have spoof email warning issue.

These steps should fix the Gmail spoof warning.

## Send emails from Gmail using the alias

This step is optional. It lets you send email from your Gmail account. The recipient will see that the email is from your alias email address, like `elegant@oncrashreboot.com`

ImprovMX has [a helpful guide](https://improvmx.com/guides/send-emails-using-gmail/) on this issue.
