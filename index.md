---
layout: default
title: Hello
---


qwe
===

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

{% highlight sh %}
echo hello
cp boom /usr/${boom}
{% endhighlight %}
