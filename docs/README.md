# A & P labs


[BIOL 206 Manual](206/206toc.md)

[BIOL 207 Manual](207/207toc.md)

 # Using in Canvas

 There are two ways to use the lab manuals in Canvas:

1. **Link to the manual**: You can link to the manual in Canvas by using the link above, or links to individual labs. When students click the link in Canvas (say, in a module), it should open in a new tab. The link above goes to a page with the full schedule and access to all labs, so it's a good option for students to bookmark. 
2. **Embed the manual**: I (Brandon) prefer to make a Canvas page with reading assignments and other prep notes like links to youtube videos or to Mastering assignments, for each page, then embed the lab manual page in that canvas page. I also provide a direct link to go direclty to the main page, but most students seem to prefer to stay within canvas. You can embed the manual in Canvas by using the "Embed" option in the Rich Content Editor, or clicking the `</>` button to edit html direclty. Paste the following in, editing the link to go to the page you wish to embed (really just have to change the lab number).  This will display the manual directly within the Canvas page, allowing students to view it without leaving Canvas.

```html
<div class="container"><iframe class="responsive-iframe" src="https://backyardbiomech.github.io/APlabs/206/lab_1.html" width="100%" height="600" loading="lazy"></iframe></div>
```

# Editing pages
If you notice a small error in the lab manual, you can edit it directly in the GitHub repository. You must have a github account and have been granted access by Brandon or Bjoern for edit permissions. 

1. Go to [https://github.com/backyardbiomech/APlabs/](https://github.com/backyardbiomech/APlabs/) and log in with your GitHub account. 
2. Navigate in the folders at the top (start in `docs`) or using the links on this page to the page you wish to edit.
3. Click the pencil icon in the top right corner of the page to edit the file. Most pages are formatted in markdown, so you can edit the text directly. If you are not familiar with markdown, you can use the [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/) to learn how to format text, links, and images. But some sections are formatted in html, so you can edit those directly as well. If you don't know either, feel free to make simple text changes (like typos) but let me (Brandon) know about formatting errors that need fixed. 
4. After making your changes, click on the green `Commit changes` button at the top. 
5. In the dialog that opens, leave the default message and settings, and just click `Commit changes`. 
6. Your changes will be reflected in the live version of the manual after a few minutes and after you refresh the page.
