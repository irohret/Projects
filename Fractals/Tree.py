<html>
<head>
<title>Tree.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #808080;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Tree.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">turtle</span>
<span class="s0">import </span><span class="s1">math</span>


<span class="s1">slider = </span><span class="s2">35.</span>
<span class="s1">branch = </span><span class="s2">100 </span><span class="s3"># aka branch_len</span>
<span class="s1">speed = </span><span class="s2">50</span>

<span class="s0">def </span><span class="s1">tree(branch_len</span><span class="s0">, </span><span class="s1">t):</span>
    <span class="s0">if </span><span class="s1">branch_len &gt; </span><span class="s2">8</span><span class="s1">:</span>
        <span class="s1">t.forward(branch_len)</span>
        <span class="s1">t.right(slider)</span>
        <span class="s3">#t.forward(branch_len)</span>
        <span class="s1">tree(branch_len * </span><span class="s2">0.7</span><span class="s0">, </span><span class="s1">t)</span>

        <span class="s1">t.left(slider * </span><span class="s2">2</span><span class="s1">)</span>
        <span class="s1">tree(branch_len * </span><span class="s2">0.7</span><span class="s0">, </span><span class="s1">t)</span>
        <span class="s1">t.right(slider)</span>

        <span class="s1">t.backward(branch_len)</span>

<span class="s0">def </span><span class="s1">main():</span>

    <span class="s1">t = turtle.Turtle()</span>
    <span class="s1">sc = turtle.Screen()</span>
    <span class="s1">t.speed(speed)</span>
    <span class="s1">t.penup()</span>
    <span class="s1">t.left(</span><span class="s2">90</span><span class="s1">)</span>
    <span class="s1">t.goto(</span><span class="s2">0</span><span class="s0">, </span><span class="s1">-</span><span class="s2">140</span><span class="s1">)</span>
    <span class="s1">t.pendown()</span>
    <span class="s3">#t.backward(branch)</span>
    <span class="s1">t.forward(branch)</span>
    <span class="s1">tree(branch</span><span class="s0">, </span><span class="s1">t)</span>


    <span class="s1">sc.exitonclick()</span>

<span class="s1">main()</span>
</pre>
</body>
</html>