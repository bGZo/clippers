---
title: "Three-Choices-New-Users-Need-to-Make-General-Logseq"
created: 2025-01-15T10:02:20
modified: 2025-01-15T11:38:23
source: "https://discuss.logseq.com/t/three-choices-new-users-need-to-make/3411"
tags:
  
tags-link:
type: "archive-web"
---

When you start using Logseq you will have a number of decisions to make. Earlier [I’ve shared my own personal workflow](https://discuss.logseq.com/t/my-logseq-workflow/2278), but reading the comments of new users in the forums I felt that people needed more guidance in setting up their own system. This post is my attempt to address that need. This is a very opinionated piece, but I try to explain my reasoning in such a way that others who have different needs will be able to make a clear-headed choice.

## First choice: to use a daily journal or not?

As far as I know, the idea of using a daily journal was first introduced to personal knowledge managers (PKM) by Roam Research. When I first started using Roam (before I switched to Logseq), I was bothered by this because I didn’t understand why I would want to use a journal if I’m taking notes organized by research topics, not a personal diary? After watching an introductory Roam Research tutorial, however, I was convinced to try using the journal approach for a week before making up my mind, and I strongly urge new users to do so as well.

To understand why journals are useful in PKMs like Logeq and Roam it is important to understand the power of tagging in this new generation of note taking applications. When you write a tag it doesn’t just add some extra metadata that can be used for filtering your notes (like Gmail or Apple Notes), rather it creates a new page devoted to that tag. That page can itself have additional notes within it. The power of this approach comes from the existence of a special section at the bottom of the page which lists all the blocks that link back to this page. The end result is that you magically create a page of all the linked text.

Let’s say I wrote one line of a poem each day (steeling from a haiku by Bashō):

- 2021-11-09
- An old silent pond \`\`\`\[\[haiku\]\]\`
- 2021-11-10
- A frog jumps into the pond— `[[haiku]]`
- 2021-11-12
- Splash! Silence again. `[[haiku]]`

Even though each of these lines appear in separate journal pages, when I go to the page “haiku” I will see the entire poem!

An advantage of this system is that when you open the app you can start taking notes right away, rather than trying to first figure out where what you are writing should go, opening that page, finding the right space to put it, and then writing. You just write first, and then add as many tags as you want.

Note: If you are writing a large amount of text and don’t want to tag each line, you can just set all of it in the outline and add the tags to the top level of that section, like so:

- my `[[haiku]]` `[[frogs]]`
- An old silent pond
- A frog jumps into the pond—
- Splash! Silence again.

This approach works well, up to a point, but at some point you might want to copy and move all these separate notes together on a page. There are a couple of approaches to doing this. The first approach is to create what some people call as “map of content” which isn’t so much a page with all of those various page snippets, but rather a page which links together various related pages in one place. Another approach is to open up a page in the sidebar, and drag and drop blocks from your journals into that page. (Or use “block refs” instead if you want to leave the original text in the context where you first wrote it.)

## Second Choice: tags, hierarchy, or page-tags?

So, as explained above, you create pages as you go by tagging items in your journal; however, you might want to add metadata to these pages to group topical pages together. For instance, you might have pages for each of your contacts. As you write you create a page for `[[Jane Smith]]` who is a cousin, and you might want to group all your family members together so you can easily find them. There are three ways Logseq allows you to do this.

### 1\. Add tags anywhere in the page.

You can just add the tag `[[family]]` anywhere in the page, and then you will create a new page that groups together all your related contacts, but you might want to use this tag for tagging plans for your family vacation, or something about someone else’s family, or an article on how the family is changing, etc. That means that the page for this tag will not be very useful for just seeing links to family contacts.

### 2\. Use hierarchy.

Logseq allows you to insert a slash into page names, creating what it calls “hierarchy.” (In Roam it is called “namespaces.”) Thus you could create `[[contact/family]]` and `[[contact/business]]` to differentiate pages with different kinds of contacts. Such pages will have two special features added to them. First, in addition to regular backlinks they will also have a section titled "Pages tagged with “contact/------” listing just the pages you wanted. (UPDATE: Seems this feature is a benefit of page-tags rather than hierarchy.) Secondly, they will also have a “hierarchy” section, letting you move up or down the hierarchy to navigate related pages.

### 3\. Use page-tags

Another option for organizing pages is to create a special block at the top of the page with `tags::` at the beginning and then a comma separated list of related tags. These tags can be in double brackets or not, as you like. (Using them can be useful for auto-completion when typing.) The advantage of this is that you can then use special queries for “page-tags” which can help you quickly find all the pages with both “family” and “contacts” in the page-tags, for instance.

#### Putting it together:

Personally, I like to use hierarchy in my page-tags. That is, I like to use them for pages/keywords that are designed to filter and query other pages, rather than in the names of those primary pages themselves. For instance, you could preface all your contacts with “contact/” (e.g. “contact/Jane Smith”) but do you really want “contact/” in those page titles? For me it is better to just add the “contact/family” tag to the page-tags as a way of filtering out and querying my contacts, rather than in the contact titles themselves.

Some people use hierarchy to distinguish between words in different semantic domains. For instance, “company/Apple” and “fruit/apple.” But personally I prefer to not use hierarchy for this, since I have no intention of having “fruit/…” before pineapple and cherries, etc. Rather I solve this problem by having “Apple (company)” and “apple (fruit)” in the title, since it is generally a one-off solution for me.

## Third choice: One graph for everything, or multiple graphs?

In a way this is really the first choice that you make, but I put it last because I think that if you use journals and page-tags in the manner described above, you don’t really need multiple graphs. One of the great benefits, for me, of using a PKM is the way in which you can just start entering text first in your journal and then worrying about where it goes afterwords, when you add page tags. Personally, my work and personal life have a lot of overlap, so it is also useful for me to be able to access the same contact pages regardless of whether I am citing them for research or making plans to meet them for lunch. The speed of just being able to go to my journal and start typing is essential for me, and if I had to switch graphs to make a note, that would slow me down. Some people worry about performance and want to divide their graphs up for that reason, but I think if there are performance issues with large graphs, the Logeq team will be tackling them quickly so I don’t worry about it too much.

## Final Notes

My choices are clear: use one graph, use the journal, and use hierarchy in page-tags to organize your pages when necessary. Others may want to make different choices, but I hope that by explaining why I made these choices new users will get a better sense of how Logseq (and other PKMs) work. For more detail, see my post about [how my entire workflow is setup](https://discuss.logseq.com/t/my-logseq-workflow/2278).
