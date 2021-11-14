import datetime

verision = "0.01"
start = datetime.datetime.now()
text0 = """
<blockquote>
“You take the blue pill...the story ends, you wake up in your bed and believe
whatever you want to believe. You take the red pill...you stay in Wonderland,
and I show you how deep the rabbit hole goes.”
</blockquote>
<br/>
-<i>The Matrix</i><br/>
<br/>
<h1>
Book 0
</h1>
<h2>
Foundation
</h2>
<br/>
<br/>
So you got this far. It’s no accident, consider yourself lucky. You’ve cleared
significant energy blocks to divine energy. When life gives you a chance to learn
lessons, it always gives you a chance to learn them the easy way first.
Visualize a video game. And every time you lose, it gets a little bit harder
and the stakes get a little higher.
But you get the challenge again, until you beat it.
<br/>The same challenge comes back later to make sure you really get it.
<br/>If I had to do it over again, (and you can’t pay me enough to do that) this is
where I would start: If a protection (❤️) spell goes awry, the worst thing that
happens is it doesn’t work as well. That isn’t true of abundance (♦️) spells.
They still work, but maybe not in the way you think. Clearing your energty 
blocks is the first line of magickal defence. 
<br/>
<br/>"Take the poison from me so my enemies' spells can do no harm."
<br/>
<br/>Significant portions of this transmission have been truncated due to bandwidth
restrictions. Access to dimensional transmissions are included in the images 
folder.
"""
text1 = """
<h1>
Book 1
</h1>
<h2>
Meditate or GTFO
</h2>
<br/>
<br/>
<br/>
<br/>
<br/>Pull out your phone. 
<br/>
<br/>That’s not the last time I’m going to ask you to do that.
<br/>
<br/>Set a timer for four minutes and twenty seconds. If you can’t meditate
continuously until the timer goes off, Stop reading and work up to it 
incrementally until you can before you continue.
"""
book1 = """
<h1>
Book 1
</h1>
<h2>
The banishing ritual ❤️
</h2>
<br/>
<br/>

<br/>
<br/>Before proceeding, it is crucial to establish an effective banishing ritual
to cleanse yourself of foreign energies. This is basic energetic hygiene.
<br/>
<br/>There are many forms of banishing ritual from all mystic paths, the important
part is that you find one that resonates with you, one that you can memorize,
and one that you can perform mentally (even if you just visualize yourself
performing) at a moments notice.
<br/>
<br/>Since Aquarian magic is intensely personal, I am unable to detail the "correct"
steps to perform; I can only show you the door, you are the one who just walk
through it. For you, it might take the form of breathing, centering and
grounding. For others, it might look like the LBRP. What matters is that any
energy you encounter is there with your consent, and must leave when asked-
and all unpleasant energy must be transmuted before transmission.
<br/>
<br/>I usually visualize myself inside a golden 3D geometric shape like a pyramid,
tetrahedron or Merkabah. Only energies for my highest good can pass through,
and all distortions are filtered to the outside. find what works for you!
<br/>
<br/>If you have such a personal ritual, perform it now. Else, find one that works
for you!
"""

html = """
<HTML>
<head>
    <title>LIBER TECHNOLIGÆ</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Coda&display=swap" rel="stylesheet">
</head>
<body style="font-family: 'Coda', cursive; background: #000; color: #0f0">
<p>
"""

html += text0 + "<br/>"
html += text1 + "<br/>"
html += book1 + "<br/>"

html += """
v{} - {}
</p>
</body>
</html<""".format(version, datetime.datetime.now().timestamp())

f = open("LIBERTECHNOLIGÆ.html", "w")
f.write(html)
f.close()

delta = datetime.datetime.now() - start
print("compiled in {}".format(delta))