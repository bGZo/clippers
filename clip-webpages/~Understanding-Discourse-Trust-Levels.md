---
title: "Understanding Discourse Trust Levels"
created: 2025-04-05T15:50:59
modified: 2025-04-05T15:50:59
source: https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/
tags:
tags-link:
type: archive-web
---

#### [Jeff Atwood](https://blog.discourse.org/author/codinghorror/)

Jun 25, 2018 • 6 min read

The user trust system is a fundamental ==cornerstone== of Discourse. Trust levels are a way of…

  * ==Sandboxing new users in your community so that they cannot accidentally hurt themselves, or other users while they are learning what to do.==
  * ==Granting experienced users more rights over time, so that they can help everyone maintain and moderate the community they generously contribute so much of their time to.==



This seemed like a great starting point for our user trust system. Thus, Discourse offers **five user trust levels**. Your current trust level is visible on your user page, and a summary of all trust levels within your community is presented on your dashboard.

> _How do users learn about the trust system?_
> 
>   * Every new user gets ==a welcome PM== mentioning the trust system and linking to this blog post, explaining that new users may be temporarily limited for safety reasons. They are also invited to start an optional [interactive training conversation with discobot](https://blog.discourse.org/2017/08/who-is-discobot/).
> 
>   * Upon transition to trust level 1, users are sent a congratulatory PM which also links to this blog post and invites the user to fill out their user profile, or start a new topic.
> 
>   * Upon transition to trust level 2, users a sent another congratulatory PM which also links to this blog post, as well as the [tips and tricks](https://blog.discourse.org/2016/12/discourse-new-user-tips-and-tricks/) blog post.
> 
>   * Upon transition to trust level 3, users are sent a longer form PM describing their new abilities and inviting them to the lounge category to meet their fellow TL3 community members. This PM also links here to this blog post.
> 
> 



## Trust Level 0 -- New

By default, all new users start out at trust level 0, meaning trust has yet to be earned. These are visitors who just created an account, and are still [learning the community norms and the way your community works](https://blog.discourse.org/2013/03/the-universal-rules-of-civilized-discourse/). New users’ abilities are restricted for safety – both theirs and yours.

(We also want to hide any “advanced” functionality from new users to make the UI less confusing for them as they gain more experience.)

Users at trust level 0 _cannot_ …

  * Send personal messages to other users
  * “Reply as new topic” via Link button (UI removed)
  * Flag posts
  * Post more than 1 image
  * Post any attachments
  * Post more than 2 hyperlinks in a post
  * Have actual links in the ‘about me’ field of their profile (will be silently and temporarily converted to plain text)
  * Mention more than 2 users in a post
  * Post more than 3 topics
  * Post more than 10 replies
  * Edit their own posts after more than 24 hours


Admins can change these limitations by searching for `newuser` and `first_day` in site settings.

## Trust Level 1 -- Basic

At Discourse, we believe reading is the most fundamental and healthy action in any community. If a new user is willing to spend a little time reading, they will quickly be promoted to the first trust level.

Get to trust level 1 by…

  * Entering at least **5** topics
  * Reading at least **30** posts
  * Spend a total of **10** minutes reading posts


Users at trust level 1 can…

  * Use all core Discourse functions; all new user restrictions are removed
  * Send PMs
  * Upload images and attachments if enabled
  * Edit wiki posts
  * Flag posts
  * Mute other users


Admins can change these thresholds by searching for `tl1` in site settings.

## Trust Level 2 -- Member

==Members keep coming back to your community over a series of weeks; they have not only read, but actively participated long and consistently enough to be trusted with full citizenship.==

Get to trust level 2 by…

  * Visiting at least **15** days, not sequentially
  * Casting at least **1** like
  * Receiving at least **1** like
  * Replying to at least **3** different topics
  * Entering at least **20** topics
  * Reading at least **100** posts
  * Spend a total of **60** minutes reading posts


Users at trust level 2 can…

  * Use the “Invite others to this topic” button for one-click onboarding of new users to participate in topics
  * Invite outside users to PMs making a group PM
  * Daily like, edit, and flag limits increased by 1.5×
  * Ignore other users
  * Edit their own posts for up to 30 days after posting


Admins can change these thresholds by searching for `tl2` in site settings.

## Trust Level 3 -- Regular

==Regulars are the backbone of your community, the most active readers and reliable contributors over a period of months, even years==. Because they're always around, they can be further trusted to help tidy up and organize the community.

To get to trust level 3, in the last 100 days…

  * Must have visited at least **50%** of days
  * Must have replied to at least **10** different non-PM topics
  * Of topics created in the last 100 days, must have viewed **25%** (capped at 500)
  * Of posts created in the last 100 days, must have read **25%** (capped at 20k)
  * Must have received **20** likes, and given **30** likes.*
  * Must not have received more than 5 spam or offensive flags (with unique posts and unique users for each, confirmed by a moderator)
  * Must not have been suspended or silenced in the last 6 months


* These likes must be across a minimum number of different users (1/5 the number), across a minimum number of different days (1/4 the number). Likes cannot be from PMs.

All of the above criteria must be true to achieve trust level 3. Furthermore, unlike other trust levels, _you can lose trust level 3 status_. If you dip below these requirements in the last 100 days, you will be demoted back to Member. However, in order to avoid constant promotion/demotion situations, there is a 2-week grace period immediately after gaining Trust Level 3 during which you will not be demoted.

Users at trust level 3 can…

  * Recategorize and rename topics
  * Access a secure category only visible to users at trust level 3 and higher
  * Have all their links followed (we remove automatic nofollow)
  * TL3 spam flags cast on TL0 user posts immediately hide the post
  * TL3 flags cast on TL0 user posts in sufficient diversity will auto-silence the user and hide all their posts
  * Make their own posts wiki (that is, editable by any TL1+ users)
  * Daily like, edit, and flag limits increased by 2×


Admins can change these thresholds by searching for TL3 in site settings.

## Trust Level 4 -- Leader

Leaders are regulars who have been around forever and seen everything. They set a positive example for the community through their actions and their posts. If you need advice, these are the folks you turn to first, and they've earned the highest level of community trust, such that they are almost ==moderators== within the community already.

Get to trust level 4 by…

  * Manual promotion by staff only
  * (Possibly via a to-be-developed election system in the future)


Users at trust level 4 can…

  * Edit all posts
  * Pin/unpin topic
  * Close topics
  * Archive topics
  * Make topics unlisted
  * Split and merge topics
  * Reset topic bump date
  * Daily like, edit, and flag limits increased by 3×
  * Any TL4 flag cast on any post immediately takes effect and hides the target post
  * Can send personal messages to an email address



We believe this trust system has been a success so far, as it leads to stronger, more ==sustainable== communities by carefully empowering members, regulars, and leaders to curate and lead their own communities. It's one of the [key community features that sets Discourse apart](https://blog.discourse.org/2021/09/community-features/) from the rest. But like everything else in Discourse, the trust system is ==evolving== over time as we gain more experience with more communities. We'll continue to update this post with any changes.

## [How Katalon Increased Community Engagement with Discourse Hosting Every day, customers are building, growing, and running successful communities powered by Discourse. Today, we’re highlighting one of them who improved how their company engages with their external community by upgrading to Discourse hosting. We had the opportunity to speak with Sara Leslie who heads up the community and ](https://blog.discourse.org/2022/10/how-katalon-increased-community-engagement-with-discourse-hosting/)


[Stella Kapakos](https://blog.discourse.org/author/therealstella/) Oct 20, 2022 • 2 min read

## [There are Two Types of Ideas – Bad Ideas and Ideas Worth Testing While push-button solutions are quick and simple, they prevent us from really understanding the landscape in front of us, identifying how to drive improvements, and exploring the optimal pathway to success. When I trot that title line out to people, it inevitably gets an intrigued look in response, but there ](https://blog.discourse.org/2022/10/there-are-two-types-of-ideas-bad-ideas-and-ideas-worth-testing/)

  * [ ![Jono Bacon](data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect fill-opacity="0"/></svg>) ](https://blog.discourse.org/author/jonobacon/)



[Jono Bacon](https://blog.discourse.org/author/jonobacon/) Oct 18, 2022 • 2 min read

## [Not Everyone Wants to Talk to Your Community Manager The greatest asset any business can have is good relationships with their customers, and communities are a powerful environment to not just foster those relationships, but to do so in an environment where the world can see how engaging, supportive, and kind you are. So how do you do that? ](https://blog.discourse.org/2022/09/not-everyone-wants-to-talk-to-your-community-manager/)

  * [ ![Jono Bacon](data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect fill-opacity="0"/></svg>) ](https://blog.discourse.org/author/jonobacon/)



[Jono Bacon](https://blog.discourse.org/author/jonobacon/) Sep 28, 2022 • 2 min read

#### [@Discourse on Twitter New features ](https://twitter.com/discourse) #### [Discourse on GitHub Cutting-edge development ](https://github.com/discourse/discourse)

Content is by-nc-sa, Discourse logo and “Discourse Forum” ®, Civilized Discourse Construction Kit, Inc. 

[Built with love, Internet style](https://www.youtube.com/watch?v=Xe1TZaElTAs) | [Privacy Information](https://blog.discourse.org/2018/06/privacy) | [Copyright Policy](https://blog.discourse.org/2018/06/copyright) | [Status](https://status.discourse.org/)

![](data:,)

* * 
