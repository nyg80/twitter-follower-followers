twitter-follower-followers
==========================

*Note: I originally wrote this as a code sample in early 2011.  The twitter API has changed so much since then that I doubt it still works, but I'm putting it up here for posterity.*

**written in [Python][], accesses the [Twitter API][] using the
[python-twitter library][]**

This python script will go through every person that you follow on
twitter, and check to see if they're following you. If they're not
following you, it will check if anyone they follow, follows you. It then
puts the results into an HTML file.

*known limitations:* the script only gets the first 5000 people
followed by anyone that you follow, for performance reasons. Due to
Twitter's rate limiting it took the script about 10 minutes to run
against an account with 193k followers, following 111 people.

 **screenshot of results:**
![screenshot of results][]

  [Python]: http://www.python.org/ "python official website"
  [Twitter API]: http://dev.twitter.com/doc "twitter API documentation"
  [python-twitter library]: http://code.google.com/p/python-twitter/
    "python-twitter"
  [screenshot of results]: http://i.imgur.com/tMKhcUi.png
