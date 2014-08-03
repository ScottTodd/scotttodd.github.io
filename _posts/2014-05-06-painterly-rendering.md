---
layout: post
title: "Painterly Rendering"
tagline: Real-time painterly rendering using WebGL.
description: ""
category: projects
tags: [Graphics, WebGL, CoffeeScript, three.js, Open Source]
title_images: [/assets/projects/painterly-rendering/magma-bunny.png, /assets/projects/painterly-rendering/the-scream.png]
---
{% include JB/setup %}

<script src="/assets/projects/painterly-rendering/script/magma-bunny.js"></script>

<div class="project-figures">
    <figure>
        <div id="glContainer" class="project-padded" height="360px" width="360px"></div>
        <figcaption>Interactive <a href="http://en.wikipedia.org/wiki/Stanford_bunny">Stanford Bunny</a> (requires WebGL)</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/the-scream.png" class="project-padded" height="360px" width="360px">
        <figcaption><a href="http://en.wikipedia.org/wiki/The_Scream"><i>The Scream</i></a> texture on a quad</figcaption>
    </figure>
</div>

<hr>

<div class="section-heading">Overview</div>

This was my final project for <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/index.php">Advanced Computer Graphics</a> and <a href="http://www.cogsci.rpi.edu/~destem/gamearch/">Game Architecture</a>. I worked with @andy-hanson on this project over a one month period. We used <a href="http://threejs.org/">three.js</a>, <a href="http://coffeescript.org/">CoffeeScript</a>, and WebGL.

Click <a href="/assets/projects/painterly-rendering/painterly-rendering.pdf">here</a> to download our full report.

<script type="text/javascript" src="/assets/js/jquery.githubRepoWidget.min.js"></script>
<div class="github-widget" data-repo="ScottTodd/PainterlyRendering"></div>

<div class="section-heading">My Contributions</div>

I implemented brush stroke layers, depth-filtering using a multi-pass rendering approach, texture sampling, and diffuse lighting on brush stroke particles. We both contributed to the write-up and I performed the LaTeX conversion. I also collected all of the models and brush stroke textures that we used.

<hr>

<div class="project-figures">
    <figure>
        <img src="/assets/projects/painterly-rendering/blue-teapot.png" class="project-padded" height="390px" width="390px">
        <figcaption><a href="http://en.wikipedia.org/wiki/Utah_teapot">Utah Teapot</a> rendered using strokes of varying saturation</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/bronze-teapot.png" class="project-padded" height="390px" width="390px">
        <figcaption>The Utah Teapot rendered to appear bronze</figcaption>
    </figure>
</div>

<hr>

<div class="project-figures">
    <figure>
        <img src="/assets/projects/painterly-rendering/grass-sphere.png" class="project-padded" height="350px" width="350px">
        <figcaption>Sphere using a grass texture</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/torus-knot.png" class="project-padded" height="330px" width="330px">
        <figcaption>Torus knot, showcasing rendering order</figcaption>
    </figure>
</div>

<hr>

<div class="project-figures">
    <figure>
        <img src="/assets/projects/painterly-rendering/bouncing-spheres.png" class="project-padded" height="370px" width="370px">
        <figcaption><a href="http://cannonjs.org/">Cannon.js</a> integration</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/bunny-steps-anim-text.gif" class="project-padded" height="360px" width="360px">
        <figcaption>Rendering process breakdown</figcaption>
    </figure>
</div>
